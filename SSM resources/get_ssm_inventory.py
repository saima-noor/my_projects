import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
list_ssm = []
for j in regions:
    try:
        print("Here are all the ssm managedinstanceinventory from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
        
        next_token = None
        while True:
            response7 = ssm_client.get_inventory(NextToken= next_token) if next_token else ssm_client.get_inventory()
                                                                            
                                                                        
            print(response7['Entities'])                                                            
            for q in response7['Entities']:
                # status_var5 = o['Overview']['Status']
                print(q['Data']['AWS:InstanceInformation']['Content'])
                for r  in q['Data']['AWS:InstanceInformation']['Content']:
                    print(r['AgentType'])
                    status_var5 = r['InstanceStatus']
                    rank = 0
                    if status_var5 == "Stopped":
                        rank = (1*7) + 10
                    # if status_var5 == "Pending":
                    #     rank = 3*6
                    if status_var5 == "Active" or status_var5 == "Terminated":
                        rank = 1*7
                    

                    list_ssm.append((r['InstanceId'], r['ResourceType'] + " Inventory", r['AgentType'],r['InstanceStatus'], rank))
        
                print(list_ssm)


            if 'NextToken' in  response7.keys():
                next_token = response7['NextToken']
            
            else:
                break

    except Exception as e:
        print ( "Exception occured ")
        print( e )
        # print("exception error" )
        continue
print




