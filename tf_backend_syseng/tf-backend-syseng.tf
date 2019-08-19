resource "aws_s3_bucket" "tf-backend-syseng" {
  bucket = "tf-backend-syseng"
  acl    = "private"

  tags = {
    Name        = "Managed"
    Environment = "Terraform"
  }
}