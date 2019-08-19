
terraform {
 backend "s3" {
 encrypt = true
 bucket = "tf-backend-syseng"
 dynamodb_table = "terraform-state-lock-dynamo"
 region = "us-east-1"
 key = "SysEng/tf-backend/terraform-state.tf"
 profile = "default"
 shared_credentials_file = "c:\\Users\\.aws\\creds\\credentials"
 }
}