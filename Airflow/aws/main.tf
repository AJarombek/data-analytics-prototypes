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

resource "aws_mwaa_environment" "sandbox" {
  name = "sandbox"
  source_bucket_arn = aws_s3_bucket.andrew-jarombek-airflow-dags.arn
  dag_s3_path = "dags/"
  execution_role_arn = ""

  network_configuration {
    security_group_ids = []
    subnet_ids = []
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