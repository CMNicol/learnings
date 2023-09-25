resource "aws_ecr_repository" "image-repo" {
  name = var.image_repository_name
  tags = {}
}