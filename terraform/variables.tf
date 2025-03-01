variable "ALPHA_VANTAGE_API_KEY" {
  description = "Alpha Vantage API key"
  type        = string
  sensitive   = true
}

variable "EODHD_API_KEY" {
  description = "EODHD API key"
  type        = string
  sensitive   = true
}

variable "S3_FIN_BUCKET" {
  description = "S3 bucket for fin data (root)"
  type        = string
  sensitive   = false
}

variable "S3_FIN_BUCKET_RAW_SCHEMA" {
  description = "S3 dir for raw data"
  type        = string
  sensitive   = false
}
