import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm list_commands from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
        list_ssm = []
        next_token = None
        while True:
            response1 = ssm_client.list_commands(NextToken= next_token) if next_token else ssm_client.list_commands()
            print(response1['Commands'])                                                            
            for cmd in response1['Commands']:
                
                status_var1 = cmd['Status']
                error_count = cmd['ErrorCount']
                target_count = cmd['TargetCount']
                completed_count = cmd['CompletedCount']
                max_currency = int(cmd['MaxConcurrency'])
                ratio1 = ((completed_count/max_currency) * target_count)
                # print(ratio3)
                rank1 = 0


                if status_var1 == "Success":
                    rank1 = 1*5 + ratio1
                if status_var1 == "Failed":
                    rank1 = (1*5) + 5 + ratio1

                list_ssm.append((cmd['CommandId'], "Commands" , cmd['DocumentName'],cmd['Status'], rank1))
    


            print(list_ssm)               

                

            

            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
            else:
                break

    except Exception as e:
        print ( "Exception occured ")
        print( e)
        # print("exception error" )
        continue
                




