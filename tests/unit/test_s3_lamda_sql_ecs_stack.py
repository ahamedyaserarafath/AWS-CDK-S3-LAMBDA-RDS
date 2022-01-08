import aws_cdk as core
import aws_cdk.assertions as assertions

from s3_lamda_sql_ecs.s3_lamda_sql_ecs_stack import S3LamdaSqlEcsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in s3_lamda_sql_ecs/s3_lamda_sql_ecs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = S3LamdaSqlEcsStack(app, "s3-lamda-sql-ecs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
