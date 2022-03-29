import boto3
import json

import botocore
# import operator
list_codecommit = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        codecommit_client = boto3.client('codecommit',region_name = j)
        
        next_token = None
        repo_per_region = []
        while True:
            response1 = codecommit_client.list_repositories(NextToken= next_token) if next_token else codecommit_client.list_repositories()
            print(response1['repositories'])                                                            
            for repo in response1['repositories']:
                
                
                print(repo['repositoryName']) 
                # print(repo['repositoryId']) 
                repo_name = repo['repositoryName']

                
                response2 = codecommit_client.get_repository(repositoryName= repo_name) 
                print(response2['repositoryMetadata'])
                # status_var = j['AutomationExecutionStatus']
                # # print(status_var)
                # rank = 0
                # if status_var == "Success":
                #     rank = 1
                # if status_var == "Failed":
                #     rank = 2

                list_codecommit.append(repo['repositoryName'])
                repo_per_region.append(repo['repositoryName'])

                
                         


            print("count  " + str(len(list_codecommit)))
            print("count per region " + str(len(repo_per_region)))

            
            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
                
            else:
                break
        print(list_codecommit)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception :
        print ( "Exception occured ")
        continue
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          