from aws_cdk import (
    Stack,
)
from aws_cdk.aws_ecs_patterns import ApplicationLoadBalancedFargateService
from aws_cdk.aws_ecs import ContainerImage

from constructs import Construct


class FirstAppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fargate_service = ApplicationLoadBalancedFargateService(
            scope=self,
            id="FirstAppService",
            task_image_options={
                "image": ContainerImage.from_registry("amazon/amazon-ecs-sample")
            },
            public_load_balancer=True,
        )