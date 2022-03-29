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
            response5 = ssm_client.list_associations(NextToken= next_token) if next_token else ssm_client.list_associations()
                                                                            
                                                                        
            print(response5['Associations'])                                                            
            for asso in response5['Associations']:
                target = asso['Targets']
                print(target)
                values = None
                for tar in asso['Targets']:
                    print(tar['Values'])

                    if tar['Values'] == ['*']:
                        print(len(tar['Values']))
                        values = (len(tar['Values']))*2*0.1
                    else: 
                        print(len(tar['Values']))
                        values = len(tar['Values'])*0.1

                print(values)
                status_var5 = asso['Overview']['Status']
                # print(status_var5)
                rank5 = 0
                if status_var5 == "Failed":
                    rank5 = 1 + 5 + values
                if status_var5 == "Pending":
                    rank5 = 1 + 5 + values
                if status_var5 == "Success":
                    rank5 = 1 + values
                

                list_ssm.append((asso['AssociationId'], "Association", asso['Name'],asso['Overview']['Status'], rank5))
    
            print(list_ssm)


            if 'NextToken' in  response5.keys():
                next_token = response5['NextToken']
            
            else:
                break

    except Exception :
        print ( "Exception occured ")
        # print( Exception )
        # print("exception error" )
        continue
print




