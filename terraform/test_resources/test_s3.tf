module "bucket"{
  source = "../modules/s3"
  bucket_name = "test_bucket"
}