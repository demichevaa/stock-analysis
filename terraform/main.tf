resource "aws_s3_bucket" "fin" {
  bucket = var.S3_FIN_BUCKET
  tags = {
    env  = "prod"
    proj = "fin-core"
  }
}

resource "aws_s3_object" "raw_folder" {
  bucket = aws_s3_bucket.fin.id
  key    = var.S3_FIN_BUCKET_RAW_SCHEMA
}
