import boto3
import json

import botocore
# import operator
list_environments = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        ebs_client = boto3.client('elasticbeanstalk',region_name = j)
        
        next_token = None
       
        while True:
            response1 = ebs_client.describe_environments(NextToken= next_token) if next_token else ebs_client.describe_environments()
            print(response1['Environments'])                                                            
            for env in response1['Environments']:
                
                
                print(env['EnvironmentName']) 
                print(env['ApplicationName']) 

                response3 = ebs_client.describe_environment_managed_actions(EnvironmentId=env['EnvironmentId'],EnvironmentName=env['EnvironmentName'], Status='Scheduled')

                print(response3)
                print(response3['ManagedActions'])
                print(len(response3['ManagedActions']))

                total_actions_scheduled = len(response3['ManagedActions']) 
                response4 = ebs_client.describe_environment_managed_actions(EnvironmentId=env['EnvironmentId'],EnvironmentName=env['EnvironmentName'], Status='Pending')

                print(response4)
                print(response4['ManagedActions'])
                print(len(response4['ManagedActions']))

                total_actions_pending = len(response4['ManagedActions']) 
                print("............................")


                print(total_actions_scheduled)

                print(total_actions_pending)
              

            #     list_environments.append(env['EnvironmentName'])
               

                
                         


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
                




