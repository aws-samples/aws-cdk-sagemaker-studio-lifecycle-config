Deploying AWS CDK constructs

*To deploy your AWS CDK stack, run the following commands in the location where you cloned the repository*

The command may be “python” instead of “python3” depending on your path configurations. 

Step 1: Create a virtual environment. 

* macOS/Linux: python3 -m venv .cdk-venv
* Windows: python3 -m venv .cdk-venv

Step 2: Activate the virtual environment.

* macOS/Linux: source .cdk-venv\bin\activate
* Windows: .cdk-venv/Scripts/activate.bat
* Powershell: .cdk-venv/Scripts/activate.ps1

Step 3: install the required dependencies. 

* pip install -r requirements.txt
* pip install -r requirements-dev.txt

*[Optional]* At this point you can now synthesize the CloudFormation template for this code.

cdk synth

Step 4: Deploy the solution

* aws configure
* cdk bootstrap 
* cdk deploy 


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

