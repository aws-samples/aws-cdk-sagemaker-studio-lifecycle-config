from typing import Optional

from constructs import Construct
from aws_cdk import (
    aws_iam as iam,
    Duration,
    custom_resources,
    CustomResource,
    aws_lambda as lambda_,
)
import json


class SageMakerStudioLifeCycleConfig(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        studio_lifecycle_config_content: str,
        studio_lifecycle_config_app_type: str,
        studio_lifecycle_config_name: str,
        studio_lifecycle_config_arn: str,
        **kwargs,
    ):
        super().__init__(scope, id)
        self.studio_lifecycle_config_content = studio_lifecycle_config_content

        self.studio_lifecycle_config_name = studio_lifecycle_config_name
        self.studio_lifecycle_config_app_type = studio_lifecycle_config_app_type

        lifecycle_config_role = iam.Role(
            self,
            "SmStudioLifeCycleConfigRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
        )

        lifecycle_config_role.add_to_policy(
            iam.PolicyStatement(
                resources=[f"arn:aws:sagemaker:{scope.region}:{scope.account}:*"],
                actions=[
                    "sagemaker:CreateStudioLifecycleConfig",
                    "sagemaker:ListUserProfiles",
                    "sagemaker:UpdateUserProfile",
                    "sagemaker:DeleteStudioLifecycleConfig",
                    "sagemaker:AddTags",
                ],
            )
        )

        create_lifecycle_script_lambda = lambda_.Function(
            self,
            "CreateLifeCycleConfigLambda",
            runtime=lambda_.Runtime.PYTHON_3_8,
            timeout=Duration.minutes(3),
            code=lambda_.Code.from_asset(
                "../mlsl-cdk-constructs-lib/src/lifecycle_config_files"
            ),
            handler="onEvent.handler",
            role=lifecycle_config_role,
            environment={
                "studio_lifecycle_config_content": self.studio_lifecycle_config_content,
                "studio_lifecycle_config_name": self.studio_lifecycle_config_name,
                "studio_lifecycle_config_app_type": self.studio_lifecycle_config_app_type,
            },
        )

        config_custom_resource_provider = custom_resources.Provider(
            self,
            "ConfigCustomResourceProvider",
            on_event_handler=create_lifecycle_script_lambda,
        )

        studio_lifecycle_config_custom_resource = CustomResource(
            self,
            "LifeCycleCustomResource",
            service_token=config_custom_resource_provider.service_token,
        )
        self.studio_lifecycle_config_arn = (
            studio_lifecycle_config_custom_resource.get_att("StudioLifecycleConfigArn")
        )

        # Format for creating a lifecycle config using the sagemaker config construct
        # studio_config_one = SageMakerStudioLifeCycleConfig(
        #     self,
        #     "Project123",
        #     studio_lifecycle_config_content="base64content",
        #     studio_lifecycle_config_name="Test",
        #     studio_lifecycle_config_app_type="JupyterServer",
        #      )
