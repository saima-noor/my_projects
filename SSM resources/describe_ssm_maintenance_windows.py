import boto3
import json

import botocore
# import operator
list_ssm =[]
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm maintenance_windows from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
        
        next_token = None
        while True:
            response6 = ssm_client.describe_maintenance_windows(NextToken= next_token) if next_token else ssm_client.describe_maintenance_windows()
            print(response6['WindowIdentities'])                                                            
            for p in response6['WindowIdentities']:
                status_var6 = p['Enabled']
                print(status_var6)
                stat = "Enabled"
                rank = 0
                if status_var6 == True:
                    rank = 2*8
                    stat = "Enabled"
                if status_var6== False:
                    rank = 0.25*8
                    stat = "Disabled"
                

                list_ssm.append((p['WindowId'], "Maintenance window", p['Description'], stat, rank))
    
            print(list_ssm)

            
            if 'NextToken' in  response6.keys():
                next_token = response6['NextToken']
                
            else:
                break

    except Exception :
        print ( "Exception occured ")
        continue
                




