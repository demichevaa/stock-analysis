resource "aws_s3_bucket" "fin" {
  bucket = "daa-fin"
  tags = {
    env  = "prod"
    proj = "fin-core"
  }
}

resource "aws_s3_object" "raw_folder" {
  bucket = aws_s3_bucket.fin.id
  key    = "raw/"
}
