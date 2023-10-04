import os
from uuid import uuid4

from aws_cdk import CfnOutput, RemovalPolicy
from aws_cdk.aws_s3 import BlockPublicAccess, Bucket, BucketAccessControl
from aws_cdk.aws_s3_deployment import BucketDeployment, Source
from constructs import Construct


class S3(Construct):
    web_bucket: Bucket
    web_bucket_deployment: BucketDeployment

    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.web_bucket = Bucket(
            scope=scope,
            id="WebBucket",
            bucket_name=f"chapter-3-web-bucket-{uuid4()}",
            website_index_document="index.html",
            website_error_document="index.html",
            public_read_access=True,
            block_public_access=BlockPublicAccess.BLOCK_ACLS,
            access_control=BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        self.web_bucket_deployment = BucketDeployment(
            scope=scope,
            id="WebBucketDeployment",
            sources=[Source.asset(os.path.abspath("../web/build"))],
            destination_bucket=self.web_bucket,
        )

        CfnOutput(
            scope=scope,
            id="FrontendUrl",
            value=self.web_bucket.bucket_website_url,
        )
