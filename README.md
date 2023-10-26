### Prerequisites

To get started, make sure you have the following prerequisites:

* AWS Command Line Interface (https://aws.amazon.com/cli/) (AWS CLI) installed
* AWS CDK (https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed, specifically Working with CDK in Python (https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
* An AWS profile with permissions to create AWS Identity and Access Management (AWS IAM) (https://aws.amazon.com/iam/) roles, Studio domains, and Studio user profiles
* Python 3+ 

### Deploying AWS CDK constructs

*To deploy your AWS CDK stack, run the following commands in the location where you cloned the repository*

The command may be “python” instead of “python3” depending on your path configurations. 

**Create a virtual environment.**

* For macOS/Linux, use python3 -m venv .cdk-venv
* For Windows, use python3 -m venv .cdk-venv

**Activate the virtual environment.**

* For macOS/Linux, use source .cdk-venv\bin\activate
* For Windows, use .cdk-venv/Scripts/activate.bat
* For Powershell, use .cdk-venv/Scripts/activate.ps1

**Install the required dependencies.**

* pip install -r requirements.txt

At this point you can optionally synthesize the CloudFormation template for this code:

cdk synth

 **Deploy the solution** 

* aws configure
* cdk bootstrap 
* cdk deploy 

## Clean up

**Delete the AWS CDK stack**

When you’re done with the resources you created, you can destroy your AWS CDK stack by running the following command in the location where you cloned the repository: 

cdk destroy

When asked to confirm the deletion of the stack, enter yes.

You can also delete the stack on the AWS CloudFormation console with the following steps:

1. Open the AWS CloudFormation console, choose Stacks in the navigation pane.
2. Choose the stack that you want to delete.
3. In the stack details pane, choose Delete.
4. Choose Delete stack when prompted.

If you run into any errors you may have to manually delete some resources depending on your account configuration. 




