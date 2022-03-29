import boto3

ec2 = boto3.client('ec2')


response = ec2.run_instances(
    ImageId='ami-087c17d1fe0178315',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
     KeyName = 'saima_kp',
     #SubnetId='subnet-a818bc86', #default subnet
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            
            'DeviceIndex': 0,
            'Groups': [
                'sg-beb328f5', #default security group
            ],
            
            'SubnetId': 'subnet-a818bc86'
        },
    ],

)

# ec2 = boto3.resource('ec2')
# #create a new ec2 instance
# instances = ec2.run_instances(
#     ImageId='ami-087c17d1fe0178315',
#     InstanceType = 't2.micro',
#     MinCount=1,
#     MaxCount=1,
#     KeyName = 'saima_kp'
#     )
