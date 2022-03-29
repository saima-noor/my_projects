import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm list_commands from "+ j +" region")
        print("..................................................................................................")


        managedinstanceinventory_client = boto3.client('ssm', region_name = j )
        list_ssm = []
        next_token = None
        while True:
            response3 = managedinstanceinventory_client.list_command_invocations(
                                                                        NextToken= next_token
                                                                    ) if next_token else managedinstanceinventory_client.list_command_invocations()
            print(response3['CommandInvocations'])                                                            
            for m in response3['CommandInvocations']:
                
                status_var3 = m['Status']
                
                rank = 0
                if status_var3 == "Success":
                    rank = 1
                if status_var3 == "Failed":
                    rank = 2

                list_ssm.append((m['CommandId'], "Commands Invocations" , m['DocumentName'],m['Status'], rank))
    


            print(list_ssm)               

                

            

            if 'NextToken' in  response3.keys():
                next_token = response3['NextToken']
            else:
                break

    except Exception :
        print ( "Exception occured ")
        # print( Exception )
        # print("exception error" )
        continue
                




