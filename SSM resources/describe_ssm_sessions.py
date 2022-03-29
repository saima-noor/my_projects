import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm sessions from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
        list_ssm = []
        next_token = None
        while True:
            response2 = ssm_client.describe_sessions(State='Active',
                                                                        NextToken= next_token
                                                                    ) if next_token else ssm_client.describe_sessions(State='Active')
            print(response2['Sessions'])                                                            
            for l in response2['Sessions']:
     
                
                status_var2 = l['Status']
                
                rank = 0
                if status_var2 == "Connected":
                    rank = 1
                if status_var2 == "Failed":
                    rank = 2

                list_ssm.append((l['SessionId'], "Sessions" , "No Document name",l['Status'], rank))
    


            print(list_ssm)
            
            if 'NextToken' in  response2.keys():
                next_token = response2['NextToken']
                
            else:
                break

    except Exception as e:
        print ( "Exception occured ")
        print(e)
        continue
                




