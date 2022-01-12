/**
 * Infrastructure creating an Apache Airflow environment on AWS.
 * Author: Andrew Jarombek
 * Date: 11/21/2021
 */

provider "aws" {
  region = "us-east-1"
}

terraform {
  required_version = ">= 1.0.0"

  required_providers {
    aws = ">= 3.66.0"
  }

  backend "s3" {
    bucket = "andrew-jarombek-terraform-state"
    encrypt = true
    key = "sandbox/data-analytics-prototypes/airflow"
    region = "us-east-1"
  }
}

locals {
  name = "sandbox"
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "aws_vpc" "application-vpc" {
  tags = {
    Name = "application-vpc"
  }
}

data "aws_subnet" "application-lily-private-subnet" {
  tags = {
    Name = "application-lily-private-subnet"
  }
}

data "aws_subnet" "application-teddy-private-subnet" {
  tags = {
    Name = "application-teddy-private-subnet"
  }
}

resource "aws_mwaa_environment" "sandbox" {
  name = local.name
  airflow_version = "2.0.2"

  source_bucket_arn = aws_s3_bucket.andrew-jarombek-airflow-dags.arn
  dag_s3_path = "dags/"
  execution_role_arn = aws_iam_role.airflow.arn

  network_configuration {
    security_group_ids = [aws_security_group.airflow.id]
    subnet_ids = [
      data.aws_subnet.application-lily-private-subnet.id,
      data.aws_subnet.application-teddy-private-subnet.id
    ]
  }

  logging_configuration {
    dag_processing_logs {
      enabled = true
      log_level = "INFO"
    }

    scheduler_logs {
      enabled = true
      log_level = "INFO"
    }

    task_logs {
      enabled = true
      log_level = "INFO"
    }

    webserver_logs {
      enabled = true
      log_level = "INFO"
    }

    worker_logs {
      enabled = true
      log_level = "INFO"
    }
  }

  tags = {
    Name = "sandbox"
    Application = "all"
    Environment = "sandbox"
  }
}

resource "aws_s3_bucket" "andrew-jarombek-airflow-dags" {
  bucket = "andrew-jarombek-airflow-dags"
  acl = "private"

  versioning {
    enabled = false
  }

  tags = {
    Name = "andrew-jarombek-airflow-dags"
    Application = "all"
    Environment = "sandbox"
  }
}

resource "aws_s3_bucket_policy" "andrew-jarombek-airflow-dags-policy" {
  bucket = aws_s3_bucket.andrew-jarombek-airflow-dags.id
  policy = jsonencode({
    Version = "2012-10-17"
    Id = "AndrewJarombekAirflowDagsPolicy"
    Statement = [
      {
        Sid = "Permissions"
        Effect = "Allow"
        Principal = {
          AWS = data.aws_caller_identity.current.account_id
        }
        Action = ["s3:*"]
        Resource = ["${aws_s3_bucket.andrew-jarombek-airflow-dags.arn}/*"]
      }
    ]
  })
}

resource "aws_s3_bucket_object" "dags" {
  for_each = fileset("../dags/", "*.py")
  bucket = aws_s3_bucket.andrew-jarombek-airflow-dags.id
  key = "dags/${each.value}"
  source = "../dags/${each.value}"
  etag = filemd5("../dags/${each.value}")
}

data "aws_iam_policy_document" "airflow-assume-role-policy" {
  statement {
    sid = "mwaa"
    actions = ["sts:AssumeRole"]

    principals {
      identifiers = ["airflow-env.amazonaws.com", "airflow.amazonaws.com"]
      type = "Service"
    }
  }
}

resource "aws_iam_role" "airflow" {
  name = "airflow"
  path = "/sample/"
  assume_role_policy = data.aws_iam_policy_document.airflow-assume-role-policy.json
}

data "aws_iam_policy_document" "airflow-policy" {
  statement {
    sid = "airflowPublishMetrics"
    actions = ["airflow:PublishMetrics"]
    effect = "Allow"
    resources = [
      "arn:aws:airflow:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:environment/${local.name}"
    ]
  }

  statement {
    sid = "airflowListBucket"
    actions = ["s3:ListAllMyBuckets"]
    effect = "Allow"
    resources = [
      aws_s3_bucket.andrew-jarombek-airflow-dags.arn,
      "${aws_s3_bucket.andrew-jarombek-airflow-dags.arn}/*"
    ]
  }

  statement {
    sid = "airflowS3"
    actions = [
      "s3:GetObject*",
      "s3:GetBucket*",
      "s3:List*"
    ]
    effect = "Allow"
    resources = [
      aws_s3_bucket.andrew-jarombek-airflow-dags.arn,
      "${aws_s3_bucket.andrew-jarombek-airflow-dags.arn}/*"
    ]
  }

  statement {
    sid = "airflowDescribeLogGroups"
    actions = ["logs:DescribeLogGroups"]
    effect = "Allow"
    resources = ["*"]
  }

  statement {
    sid = "airflowLogs"
    actions = [
      "logs:CreateLogStream",
      "logs:CreateLogGroup",
      "logs:PutLogEvents",
      "logs:GetLogEvents",
      "logs:GetLogRecord",
      "logs:GetLogGroupFields",
      "logs:GetQueryResults",
      "logs:DescribeLogGroups"
    ]
    effect = "Allow"
    resources = ["arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:airflow-${local.name}*"]
  }

  statement {
    sid = "airflowMetricData"
    actions = ["cloudwatch:PutMetricData"]
    effect = "Allow"
    resources = ["*"]
  }

  statement {
    sid = "airflowSqs"
    actions = [
      "sqs:ChangeMessageVisibility",
      "sqs:DeleteMessage",
      "sqs:GetQueueAttributes",
      "sqs:GetQueueUrl",
      "sqs:ReceiveMessage",
      "sqs:SendMessage"
    ]
    effect = "Allow"
    resources = ["arn:aws:sqs:${data.aws_region.current.name}:*:airflow-celery-*"]
  }

  statement {
    sid = "airflowKms"
    actions = [
      "kms:Decrypt",
      "kms:DescribeKey",
      "kms:GenerateDataKey*",
      "kms:Encrypt"
    ]
    effect = "Allow"
    not_resources = ["arn:aws:kms:*:${data.aws_region.current.name}:key/*"]

    condition {
      test = "StringLike"
      variable = "kms:ViaService"
      values = ["sqs.${data.aws_region.current.name}.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy" "airflow" {
  name = "airflow"
  path = "/sample/"
  policy = data.aws_iam_policy_document.airflow-policy.json
}

resource "aws_iam_role_policy_attachment" "airflow" {
  policy_arn = aws_iam_policy.airflow.arn
  role = aws_iam_role.airflow.name
}

resource "aws_security_group" "airflow" {
  name = "airflow-sample"
  description = "Security Group for an Amazon MWAA sample environment"
  vpc_id = data.aws_vpc.application-vpc.id

  ingress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    self = true
  }

  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "airflow-sample"
    Application = "all"
    Environment = "sandbox"
  }
}