import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm ComplianceItems from "+ j +" region")
        print("..................................................................................................")


        managedinstanceinventory_client = boto3.client('ssm', region_name = j )
        managedinstanceinventory = []
        next_token = None
        while True:
            response = managedinstanceinventory_client.list_compliance_items(ResourceIds=['i-0b09826c077d14709'],
                                                                        NextToken= next_token
                                                                    ) if next_token else managedinstanceinventory_client.list_compliance_items(ResourceIds=['i-0b09826c077d14709'])
            print(response['ComplianceItems'])                                                            
            for i in response['ComplianceItems']:
                #if i['Name'] == "AWS-GatherSoftwareInventory":   #check if the association is created to configure an inventory to collect metadata . i['Name'] is the documant name for the association
                managedinstanceinventory.append(i['ComplianceType'])
                
                # print(i['ComplianceType']) # name of the association

                


            print("count ---- " + str(len(managedinstanceinventory)))
            #print(response['pipelines'])
            # print(managedinstanceinventory)

            if 'NextToken' in  response.keys():
                next_token = response['NextToken']
                # funcs_arn.append(i['FunctionArn'])
                # print(funcs_arn)
            else:
                break

    except Exception :
        print ( "Exception occured ")
        # print( Exception )
        # print("exception error" )
        continue
                




