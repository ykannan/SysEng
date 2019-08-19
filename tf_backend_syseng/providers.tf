provider "aws" {
  region  = "${var.region}"
  profile = "${var.profile}"
  version = "~> 2.0"
  shared_credentials_file = "${var.creds}"
}