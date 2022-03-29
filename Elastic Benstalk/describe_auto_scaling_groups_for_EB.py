import boto3
import json

import botocore
# import operator
list_environments = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the EB Environments from "+ j +" region")
        print("..................................................................................................")


        auto_client = boto3.client('autoscaling',region_name = j)
        
        next_token = None
       
        while True:
            response1 = auto_client.describe_auto_scaling_groups(  NextToken= next_token) if next_token else auto_client.describe_auto_scaling_groups()
            print(response1['AutoScalingGroups'])                                                            
            for env in response1['AutoScalingGroups']:
                
                #AutoScalingGroupNames= ['awseb-e-aq3frxmmmv-stack-AWSEBAutoScalingGroup-VQQBMVPVQ1AV']
                print(env['AutoScalingGroupName']) 
                print(env['AutoScalingGroupARN'])

                # list_environments.append((env['EnvironmentName'],status, abortableOperation, health, healthStatus, rank))
               

                
                         


            # print(" total count of environtments " + str(len(list_environments)))
            # # print("count per region " + str(len(repo_per_region)))

            
            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
                
            else:
                break
        # print(list_environments)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception as e :
        print ( "Exception occured ")
        print(e)
        continue
                




