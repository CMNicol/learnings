import boto3


CLUSTER = "shortname"
CONTAINER_INSTANCES = ["container instance IDs"]
NETWORK_CONFIG = {}
TASK_DEFINITION = "family:revision or ARN"


ecs = boto3.client("ecs")

response = ecs.start_task(
    taskDefinition=TASK_DEFINITION,
    cluster=CLUSTER,
    containerInstances=CONTAINER_INSTANCES,
    networkConfiguration=NETWORK_CONFIG,
)
