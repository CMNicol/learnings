import os

from aws_cdk import CfnOutput, Duration
from aws_cdk.aws_ec2 import InstanceType, Vpc
from aws_cdk.aws_ecs import (
    Cluster,
    ContainerDefinition,
    ContainerImage,
    FargateService,
    FargateTaskDefinition,
    LogDriver,
    Protocol,
    PortMapping
)
from aws_cdk.aws_elasticloadbalancingv2 import (
    ApplicationListener,
    ApplicationLoadBalancer,
)
from constructs import Construct

from infrastructure.constructs.dynamodb import DynamoDb


class ECS(Construct):
    vpc: Vpc
    cluster: Cluster
    task_definition: FargateTaskDefinition
    container: ContainerDefinition
    service: FargateService
    load_balancer: ApplicationLoadBalancer
    listener: ApplicationListener

    def __init__(self, scope: Construct, construct_id: str, ddb: DynamoDb, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = Vpc(scope, "Vpc", max_azs=2)
        self.cluster = Cluster(scope, "EcsCluster", vpc=self.vpc)
        self.cluster.add_capacity(
            "DefaultAutoScalingGroup", instance_type=InstanceType("t2.micro")
        )
        self.task_definition = FargateTaskDefinition(
            scope=scope,
            id="TaskDefinition",
        )
        self.container = self.task_definition.add_container(
            "Flask",
            image=ContainerImage.from_asset(os.path.abspath("../server")),
            memory_limit_mib=256,
            logging=LogDriver.aws_logs(stream_prefix="chapter3"),
        )
        self.container.add_port_mappings(
            PortMapping(container_port=80, protocol=Protocol.TCP)
        )
        self.service = FargateService(
            scope=scope,
            id="Service",
            cluster=self.cluster,
            task_definition=self.task_definition,
        )
        self.load_balancer = ApplicationLoadBalancer(
            scope=scope,
            id="LoadBalancer",
            vpc=self.vpc,
            internet_facing=True,
        )
        self.listener = self.load_balancer.add_listener(
            "PublicListener", port=80, open=True
        )
        self.listener.add_targets(
            "ECS",
            port=80,
            targets=[
                self.service.load_balancer_target(
                    container_name="Flask", container_port=80
                )
            ],
            health_check={
                "interval": Duration.seconds(60),
                "path": "/healthcheck",
                "timeout": Duration.seconds(5),
            },
        )

        ddb.main_table.grant_read_write_data(self.task_definition.task_role)

        CfnOutput(scope, "BackendUrl", value=self.load_balancer.load_balancer_dns_name)
