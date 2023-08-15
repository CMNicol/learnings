variable "aws_region" {
  description = "AWS region for all resources."

  type    = string
  default = "eu-west-1"
}


variable "source_code_dir" {
  description = "The source code directory."
  type        = string
  default     = "hello_world"
}

variable "source_code_mod" {
  description = "The entrypoint module."
  type        = string
  default     = "hello"
}

variable "lambda_runtime" {
  description = "The lambda runtime."
  type        = string
  default     = "python3.10"
}
