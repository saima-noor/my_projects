
import boto3

ec2 = boto3.client('ec2')


response3 = ec2.terminate_instances(
    InstanceIds=[
        'i-08dabadbbe6c8dd5a',
    ]
)