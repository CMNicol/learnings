import aws_cdk as core
import aws_cdk.assertions as assertions

from first_app.first_app_stack import FirstAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in first_app/first_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FirstAppStack(app, "first-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
