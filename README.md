# Create VPC, S3, LAMDA and RDS instance with AWS CDK Python

This is a project to create a new VPC, S3, LAMDA and RDS instance on AWS with the AWS Cloud Development Kit.

This project also demonstrates:
* Create S3 bucket(Please change the name for your usage)
* Create VPC two PUBLIC subnets: PUBLIC
* Create RDS instance (MySQL multi-AZ Free tier)
* Create security group and allow access.
* Create the Lamda function(Python) with s3 tigger
    - Whenever csv file is uploaded in the respecitive s3 file will be parsed and data will be pushed to RDS
* Granting the access to RDS from lamda function


# Steps to deploy the Stack

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To deploy the stack

```
$ cdk deploy S3LamdaRDSStack
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
