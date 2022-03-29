import boto3
import json

import botocore
# import operator
list_users = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        iam_client = boto3.client('iam',region_name = j)
        
        marker = None
        # repo_per_region = []
        while True:
            response1 = iam_client.list_users(Marker= marker) if marker else iam_client.list_users()
            print(response1['Users'])                                                            
            for user in response1['Users']:
                
                
                print(user['UserName']) 
                print(user['UserId']) 

                
                
                # status_var = j['AutomationExecutionStatus']
                # # print(status_var)
                # rank = 0
                # if status_var == "Success":
                #     rank = 1
                # if status_var == "Failed":
                #     rank = 2

                list_users.append(user['UserName'])
                # repo_per_region.append(user['repositoryName'])

                
                         


            print("count  " + str(len(list_users)))
            # print("count per region " + str(len(repo_per_region)))

            
            if 'Marker' in  response1.keys():
                marker = response1['Marker']
                
            else:
                break
        print(list_users)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception as e :
        print ( "Exception occured ")
        print(e)
        continue
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          