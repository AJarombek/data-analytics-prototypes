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

data "aws_caller_identity" "current" {}

data "aws_vpc" "application-vpc" {
  tags = {
    Name = "application-vpc"
  }
}

data "aws_subnet" "kubernetes-dotty-public-subnet" {
  tags = {
    Name = "kubernetes-dotty-public-subnet"
  }
}

data "aws_subnet" "kubernetes-grandmas-blanket-public-subnet" {
  tags = {
    Name = "kubernetes-grandmas-blanket-public-subnet"
  }
}

resource "aws_mwaa_environment" "sandbox" {
  name = "sandbox"
  airflow_version = "2.0.2"

  source_bucket_arn = aws_s3_bucket.andrew-jarombek-airflow-dags.arn
  dag_s3_path = "dags/"
  execution_role_arn = aws_iam_role.airflow.arn

  network_configuration {
    security_group_ids = [aws_security_group.airflow.id]
    subnet_ids = [
      data.aws_subnet.kubernetes-dotty-public-subnet.id,
      data.aws_subnet.kubernetes-grandmas-blanket-public-subnet.id
    ]
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

data "aws_iam_policy_document" "airflow-assume-role-policy" {
  statement {
    sid = "mwaa"
    actions = ["sts:AssumeRole"]

    principals {
      identifiers = ["airflow-env.amazonaws.com", "airflow.amazonaws.com"]
      type = "service"
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