

# resource "aws_scheduler_schedule" "example" {
#   name       = "my-schedule"
#   group_name = "default"

#   flexible_time_window {
#     mode = "OFF"
#   }

#   schedule_expression = "rate(1 hours)"

#   target {
#     arn      = aws_sqs_queue.example.arn
#     role_arn = aws_iam_role.example.arn
#   }
# }

# resource "aws_sqs_queue" "example" {}

# resource "aws_scheduler_schedule" "example" {
#   name = "my-schedule"

#   flexible_time_window {
#     mode = "OFF"
#   }

#   schedule_expression = "rate(1 hours)"

#   target {
#     arn      = "arn:aws:scheduler:::aws-sdk:sqs:sendMessage"
#     role_arn = aws_iam_role.example.arn

#     input = jsonencode({
#       MessageBody = "Greetings, programs!"
#       QueueUrl    = aws_sqs_queue.example.url
#     })
#   }
# }