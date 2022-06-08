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
  region  = "us-west-2"
}

variable "vpc_cidr" { }
variable "redshift_subnet_cidr" { }
variable "rs_cluster_identifier" { }
variable "rs_database_name" { }
variable "rs_master_username" { }
variable "rs_master_pass" { }
variable "rs_nodetype" { }
variable "rs_cluster_type" { }

/*
resource "aws_vpc" "redshift_vpc" {
  cidr_block = var.vpc_cidr
  enable_dns_hostnames = true
}

resource "aws_internet_gateway" "redshift_vpc_gw" {
  vpc_id = aws_vpc.redshift_vpc.id
  depends_on = [
   aws_vpc.redshift_vpc
  ]
}

resource "aws_default_security_group" "redshift_security_group" {
  vpc_id     = aws_vpc.redshift_vpc.id
  ingress {
    from_port   = 5439
    to_port     = 5439
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  depends_on = [
    aws_vpc.redshift_vpc
  ]
}

resource "aws_subnet" "redshift_subnet" {
  vpc_id     = aws_vpc.redshift_vpc.id
  cidr_block = var.redshift_subnet_cidr
  availability_zone = "us-west-2a"
  map_public_ip_on_launch = "true"
  depends_on = [
    aws_vpc.redshift_vpc
  ]
}

resource "aws_default_route_table" "redshift_route_table" {
  default_route_table_id = aws_vpc.redshift_vpc.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.redshift_vpc_gw.id
  }
  depends_on = [
    aws_vpc.redshift_vpc
  ]
}

resource "aws_route_table_association" "redshift_route_table_association" {
  subnet_id = aws_subnet.redshift_subnet.id
  route_table_id = aws_default_route_table.redshift_route_table.id
  depends_on = [
    aws_vpc.redshift_vpc
  ]
}

resource "aws_redshift_subnet_group" "redshift_subnet_group" {
  name       = "redshift-subnet-group"
  subnet_ids = [aws_subnet.redshift_subnet.id]
  depends_on = [
    aws_vpc.redshift_vpc
  ]
}
*/

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
  //cluster_subnet_group_name = aws_redshift_subnet_group.redshift_subnet_group.id
  skip_final_snapshot       = true
  iam_roles                 = [aws_iam_role.redshift_role.arn]

  /*depends_on = [
    aws_vpc.redshift_vpc,
    aws_default_security_group.redshift_security_group,
    aws_redshift_subnet_group.redshift_subnet_group,
    aws_iam_role.redshift_role
  ]*/
}