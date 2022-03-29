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
        approvalrules_per_repo = []
        while True:
            response4 = {}
            response1 = codecommit_client.list_repositories(nextToken= next_token) if next_token else codecommit_client.list_repositories()
            print(response1['repositories'])                                                            
            for repo in response1['repositories']:

                 
                print(repo['repositoryName']) 
                next_token4 = None
          
                response4 = codecommit_client.list_associated_approval_rule_templates_for_repository(repositoryName=repo['repositoryName'],nextToken= next_token4) if next_token4 else codecommit_client.list_associated_approval_rule_templates_for_repository(repositoryName=repo['repositoryName'])

                print(response4['approvalRuleTemplateNames'])
                print("total count of approval rules for repo "  + repo['repositoryName'] + "  " + str(len(response4['approvalRuleTemplateNames'])))
                approvalrule_count = len(response4['approvalRuleTemplateNames'])
                
              

                list_codecommit.append((repo['repositoryName'],approvalrule_count ))
                approvalrules_per_repo.append(repo['repositoryName'])


            print("total count of repo " + str(len(list_codecommit)))
            print("count of repo per region " + str(len(approvalrules_per_repo)))

            
            if 'nextToken' in  response1.keys():
                next_token = response1['nextToken']
            if 'nextToken' in  response4.keys():
                next_token4 = response4['nextToken']               
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
          