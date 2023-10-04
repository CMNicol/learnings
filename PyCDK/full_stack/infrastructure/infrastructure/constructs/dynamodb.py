from aws_cdk import RemovalPolicy
from aws_cdk.aws_dynamodb import AttributeType, BillingMode, Table
from constructs import Construct


class DynamoDb(Construct):
    main_table: Table

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.main_table = Table(
            scope=scope,
            id="MainTable",
            partition_key={"name": "partition_table", "type": AttributeType.STRING},
            sort_key={"name": "sort_key", "type": AttributeType.STRING},
            table_name="main_table",
            billing_mode=BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
