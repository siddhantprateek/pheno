import pulumi
from pulumi_aws import aws

import pulumi_aws as aws

instance = aws.ec2.Instance(
    "pheno-inst", 
    instance_type="t2.micro",
    ami="ami-0f5ee92e2d63afc18",
)

pulumi.export("public_ip", instance.public_ip)
