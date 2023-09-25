# IAM
resource "aws_iam_role" "ecsTaskExecutionRole" {
  name               = "${var.infra_identifier}-execution-task-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecsTaskExecutionRole_policy" {
  role       = aws_iam_role.ecsTaskExecutionRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role"
}

# Cluster
resource "aws_ecs_cluster" "aws-ecs-cluster" {
  name = "${var.infra_identifier}-cluster"
}

resource "aws_cloudwatch_log_group" "log-group" {
  name = "${var.infra_identifier}-container-logs"
}


# Task Definition
resource "aws_ecs_task_definition" "aws-ecs-task" {
  family = "${var.infra_identifier}-task"

  container_definitions = <<DEFINITION
[
    {
        "name" : "${var.infra_identifier}-container",
        "image" : "${aws_ecr_repository.image-repo.repository_url}:latest",
        "entryPoint" : [],
        "essential" : true,
        "logConfiguration" : {
        "logDriver" : "awslogs",
        "options" : {
            "awslogs-group" : "${aws_cloudwatch_log_group.log-group.id}",
            "awslogs-region" : "${var.aws_region}",
            "awslogs-stream-prefix" : "${var.infra_identifier}"
        }
        },
        "portMappings" : [
        {
            "containerPort" : 8080,
            "hostPort" : 8080
        }
        ],
        "cpu" : 256,
        "memory" : 512,
        "networkMode" : "awsvpc"
    }
]
DEFINITION

  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  memory                   = "512"
  cpu                      = "256"
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn
  task_role_arn            = aws_iam_role.ecsTaskExecutionRole.arn
}
