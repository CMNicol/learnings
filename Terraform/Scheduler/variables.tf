variable "image_name" {
  description = "Name of image with job code."
  type        = string
  default     = "placeholder"
}

variable "image_repository_name" {
  description = "Name of ECR image repository."
  type        = string
  default     = "job-image"
}

variable "infra_identifier" {
    description = "An identifier to use in resource names."
    type = string
    default = "job-scheduler"
}

variable "aws_region" {
    description = "AWS Region"
    type = string
    default = "eu-west-1"
}
