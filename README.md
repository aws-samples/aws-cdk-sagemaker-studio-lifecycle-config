### Prerequisites

To get started, make sure you have the following prerequisites:

* AWS Command Line Interface (https://aws.amazon.com/cli/) (AWS CLI) installed
* AWS CDK (https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed, specifically Working with CDK in Python (https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
* An AWS profile with permissions to create AWS Identity and Access Management (AWS IAM) (https://aws.amazon.com/iam/) roles, Studio domains, and Studio user profiles
* Python 3+ 

### Deploying AWS CDK constructs

*To deploy your AWS CDK stack, run the following commands in the location where you cloned the repository*

The command may be “python” instead of “python3” depending on your path configurations. 

**Step 1: Create a virtual environment.**

* macOS/Linux: python3 -m venv .cdk-venv
* Windows: python3 -m venv .cdk-venv

**Step 2: Activate the virtual environment.**

* macOS/Linux: source .cdk-venv\bin\activate
* Windows: .cdk-venv/Scripts/activate.bat
* Powershell: .cdk-venv/Scripts/activate.ps1

**Step 3: install the required dependencies.**

* pip install -r requirements.txt
* pip install -r requirements-dev.txt

*[Optional]* At this point you can now synthesize the CloudFormation template for this code.

cdk synth

 **Step 4: Deploy the solution** 

* aws configure
* cdk bootstrap 
* cdk deploy 

## Clean up

To avoid ongoing charges for resources you created destroy your AWS CDK stack by running the following commands in the location where you have cloned the repository: 
cdk destroy

When asked to confirm the deletion of the stack, select yes.

Also, the stack can be deleted from the AWS Management console by performing the below actions:

To delete a stack

1. Open the AWS CloudFormation console (http:// https://console.aws.amazon.com/cloudformation) 
2. On the Stacks page in the CloudFormation console, select the stack that you want to delete.
3. In the stack details pane, choose Delete.
4. Select Delete stack when prompted.

If you run into any errors you may have to manually delete some resources depending on your account configuration. 



