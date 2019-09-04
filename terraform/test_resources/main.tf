
terraform {
 backend "s3" {
 encrypt = true
 bucket = "tf-backend-syseng"
 dynamodb_table = "terraform-state-lock-dynamo"
 region = "us-east-1"
 key = "SysEng/test_resources/terraform-state.tf"
 profile = "default"
 }
}