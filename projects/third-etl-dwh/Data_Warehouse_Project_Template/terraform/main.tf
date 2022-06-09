terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
}

variable "vpc_cidr" { }
variable "redshift_subnet_cidr" { }
variable "rs_cluster_identifier" { }
variable "rs_database_name" { }
variable "rs_master_username" { }
variable "rs_master_pass" { }
variable "rs_nodetype" { }
variable "rs_cluster_type" { }


resource "aws_iam_role_policy" "s3_full_access_policy" {
  name = "s3_full_access_policy"
  role = aws_iam_role.redshift_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "s3:*"
        Resource = "*"
      },
    ]
  })
}

resource "aws_iam_role" "redshift_role" {
  name = "redshift_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "redshift.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_redshift_cluster" "dwh" {
  cluster_identifier        = var.rs_cluster_identifier
  database_name             = var.rs_database_name
  master_username           = var.rs_master_username
  master_password           = var.rs_master_pass
  node_type                 = var.rs_nodetype
  cluster_type              = var.rs_cluster_type
  skip_final_snapshot       = true
  publicly_accessible       = true
  iam_roles                 = [aws_iam_role.redshift_role.arn]
}