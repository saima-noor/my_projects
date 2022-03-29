import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm available patches from "+ j +" region")
        print("..................................................................................................")


        managedinstanceinventory_client = boto3.client('ssm', region_name = j )
        managedinstanceinventory = []
        next_token = None
        while True:
            response = managedinstanceinventory_client.describe_available_patches(
                                                                        NextToken= next_token
                                                                    ) if next_token else managedinstanceinventory_client.describe_available_patches()
            # print(response['Patches'])                                                            
            for i in response['Patches']:
                
                managedinstanceinventory.append(i['Id'])
                print(i['Id']) 
                
                # for compliance in i['CompliantSummary']:
                #     print("Count of compliants: ") 
                #     print(str(compliance['CompliantCount']))
                # for non_compliance in i['NonCompliantSummary']:
                #     print("Count of non-compliants: ") 
                #     print(non_compliance['NonCompliantCount'])                


            print("count  " + str(len(managedinstanceinventory)))
            
            if 'NextToken' in  response.keys():
                next_token = response['NextToken']
                
            else:
                break

    except Exception :
        print ( "Exception occured ")
        continue
                




