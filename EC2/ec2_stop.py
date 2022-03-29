import boto3

ec2 = boto3.client('ec2')

response5 = ec2.stop_instances(
    InstanceIds=[
        'i-08dabadbbe6c8dd5a'
    ]
)