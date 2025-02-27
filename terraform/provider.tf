terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.88.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-1"
  default_tags {
    tags = {
      proj      = "fin-core"
      env       = "prod"
      manged-by = "terraform"
    }
  }
}
