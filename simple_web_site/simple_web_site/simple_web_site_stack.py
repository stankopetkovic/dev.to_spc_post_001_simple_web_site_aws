from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_lambda_python_alpha as lambda_python,
)
from constructs import Construct

class SimpleWebSiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        web_site_lambda = lambda_python.PythonFunction(
            self,
            "web_site_lambda",
            function_name="flask-lambda",
            entry="simple_web_site/web_site_lambda",
            index="handler.py",
            handler="handler",
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout=Duration.seconds(30),
        )
