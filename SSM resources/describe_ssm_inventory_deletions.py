import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm inventory_deletions from "+ j +" region")
        print("..................................................................................................")


        managedinstanceinventory_client = boto3.client('ssm', region_name = j )
        managedinstanceinventory = []
        next_token = None
        while True:
            response = managedinstanceinventory_client.describe_inventory_deletions(
                                                                        NextToken= next_token
                                                                    ) if next_token else managedinstanceinventory_client.describe_inventory_deletions()
            print(response['InventoryDeletions'])                                                            
            for i in response['InventoryDeletions']:
                #if i['Name'] == "AWS-GatherSoftwareInventory":   #check if the association is created to configure an inventory to collect metadata . i['Name'] is the documant name for the association
                managedinstanceinventory.append(i['DeletionId'])
                #print(i['Name'] ) #document name
                # print(response['Associations'])
                print(i['DeletionId']) # name of the association

                


                #arn = i['name']
                #print(len(i['FunctionArn']))
                #print(arn)
                #print(response)
        


       
                # elements = arn.split(':', 5)
                # result = {
                #     'arn': elements[0],
                #     'partition': elements[1],
                #     'service': elements[2],
                #     'region': elements[3],
                #     'account': elements[4],
                #     'resource_name': elements[5],
                #     'resource_type': None
                #     }
                # #print(elements)

                # #regions = []
                # if '/' in result['resource_name']:
                #     result['resource_type'], result['resource_name'] = result['resource_name'].split('/',1)
                # elif ':' in result['resource_name']:
                #     result['resource_type'], result['resource_name'] = result['resource_name'].split(':',1)

                # # print(result['region'])
                # # print(result['resource_type'])

                # # regions.append(result['region'])
                # # print(len(regions))

            print("count ---- " + str(len(managedinstanceinventory)))
            #print(response['pipelines'])

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
                




