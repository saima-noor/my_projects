import boto3

ec2 = boto3.client('ec2')

response2 = ec2.describe_instances()
print(response2)