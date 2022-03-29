import boto3
import json

import botocore
# import operator
list_ssm = []
automation_execution_id = []
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        automation_executions_client = boto3.client('ssm', region_name = j )
        
        next_token = None
        while True:
            response1 = automation_executions_client.describe_automation_executions(
                                                                        NextToken= next_token
                                                                    ) if next_token else automation_executions_client.describe_automation_executions()
            print(response1['AutomationExecutionMetadataList'])                                                            
            for j in response1['AutomationExecutionMetadataList']:
                
                
                print(j['AutomationExecutionId']) 
                automation_execution_id.append(j['AutomationExecutionId'])
                
                status_var = j['AutomationExecutionStatus']
                # print(status_var)
                rank = 0
                if status_var == "Success":
                    rank = 1
                if status_var == "Failed":
                    rank = 2

                list_ssm.append((j['AutomationExecutionId'], "Automation Execution" ,j['DocumentName'],j['AutomationExecutionStatus'], rank))

                
                         


            print("count  " + str(len(list_ssm)))
            
            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
                
            else:
                break
        print(list_ssm)
        print(automation_execution_id)
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception :
        print ( "Exception occured ")
        continue
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          