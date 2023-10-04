from aws_cdk import Stack
from constructs import Construct

from infrastructure.constructs.dynamodb import DynamoDb
from infrastructure.constructs.ecs import ECS
from infrastructure.constructs.s3 import S3


class InfrastructureStack(Stack):
    dynamodb: DynamoDb
    s3: S3
    ecs: ECS

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.dynamodb = DynamoDb(self, "DynamoDb")
        self.s3 = S3(self, "S3")
        self.ecs = ECS(self, "ECS", self.dynamodb)
