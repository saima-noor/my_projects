import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm parameters from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
        list_ssm = []
        next_token = None
        while True:
            response4 = ssm_client.describe_parameters(
                                                                        NextToken= next_token
                                                                    ) if next_token else ssm_client.describe_parameters()
            print(response4['Parameters'])                                                            

            for n in response4['Parameters']:
                
                status_var4 = n['Tier']
                
                rank = 0
                if status_var4 == "Standard":
                    rank = 2
                if status_var4 == "Advanced" or status_var4 == "Intelligent-Tiering":
                    rank = 1
                

                list_ssm.append((n['Name'], n['Type']+ " Parameter" , n['Description'],n['Tier'], rank))
    
            print(list_ssm)
                
             

          

            # print("count ---- " + str(len(managedinstanceinventory)))
            #print(response['pipelines'])

            if 'NextToken' in  response4.keys():
                next_token = response4['NextToken']
                
            else:
                break

    except Exception :
        print ( "Exception occured ")
        
        continue
                




