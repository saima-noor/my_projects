import boto3

ec2 = boto3.client('ec2')
response4 = ec2.start_instances(
    InstanceIds=[
        'i-08dabadbbe6c8dd5a'
    ]
)