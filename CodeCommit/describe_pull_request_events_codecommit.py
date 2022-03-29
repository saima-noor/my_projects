from itertools import count
import boto3
import json

import botocore
# import operator
list_codecommit = []
account_id_list = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        codecommit_client = boto3.client('codecommit',region_name = j)
        
        next_token = None
        pullrequests_per_repo = []
        
        while True:
            response3 = {}
            response4 = {}
            response1 = codecommit_client.list_repositories(nextToken= next_token) if next_token else codecommit_client.list_repositories()
            print(response1['repositories']) 
                                                                      
            for repo in response1['repositories']:
                pull_req_events_per_repo = []


                print("NAme of the repository::::::::::::::")
                print(repo['repositoryName']) 
                next_token3 = None

                response2 = codecommit_client.get_repository(
                repositoryName=repo['repositoryName'])
                print("Account id of : " + repo['repositoryName'])

                print(response2['repositoryMetadata']['accountId'])
                account_id = response2['repositoryMetadata']['accountId']

          
                response3 = codecommit_client.list_pull_requests(repositoryName=repo['repositoryName'],nextToken= next_token3) if next_token3 else codecommit_client.list_pull_requests(repositoryName=repo['repositoryName'])
                print(response3)
                print("pull requests info::::::::::::::")

                print(response3['pullRequestIds'])
                print("total count of pull requests for repo "  + repo['repositoryName'] + "  " + str(len(response3['pullRequestIds'])))
                pullrequests_count = len(response3['pullRequestIds'])
                pullreq_id = response3['pullRequestIds']
                print("content length::::::::::::::::")
                print(response3['ResponseMetadata']['HTTPHeaders']['content-length'])  
                content_len = response3['ResponseMetadata']['HTTPHeaders']['content-length']
                pull_req_events_count = None
                event_type_priority = []

                if pullrequests_count != 0:            

                    for req in pullreq_id:
                        # pull_req_events = []

                    
                        response4 = codecommit_client.describe_pull_request_events(pullRequestId= req)
                        print(response4)
                        print("events of a pull request info::::::::::::")
                        print(response4['pullRequestEvents'])
                        print("count of events per pull request in a repo "  + repo['repositoryName'] + "  " + str(len(response4['pullRequestEvents'])))

                        pull_req_events_count = len(response4['pullRequestEvents'])
                        pull_req_events_per_repo.append(pull_req_events_count)

                        

                        for events in response4['pullRequestEvents']:
                            print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                            if events['pullRequestEventType']== "PULL_REQUEST_CREATED" or events['pullRequestEventType']== "PULL_REQUEST_APPROVAL_RULE_CREATED" or events['pullRequestEventType']== "PULL_REQUEST_APPROVAL_RULE_DELETED":
                                event_type_priority.append(2)
                            if events['pullRequestEventType']== "PULL_REQUEST_APPROVAL_RULE_OVERRIDDEN" or  events['pullRequestEventType']=="PULL_REQUEST_APPROVAL_RULE_UPDATED" or events['pullRequestEventType']== "PULL_REQUEST_SOURCE_REFERENCE_UPDATED":
                                event_type_priority.append(3)
                            if events['pullRequestEventType']== "PULL_REQUEST_MERGE_STATE_CHANGED" or events['pullRequestEventType']== "PULL_REQUEST_APPROVAL_STATE_CHANGED" or events['pullRequestEventType']== "PULL_REQUEST_STATUS_CHANGED":
                                event_type_priority.append(4)

                    print(event_type_priority)
                                                                                                                                                                                                                                                                         
                        

                        # print("count of pull request events:  " +str(len(pull_req_events_count)))

                else:
                    pull_req_events_count = 0
                    pull_req_events_per_repo.append(pull_req_events_count)

                pull_req_events_count_per_repo_sum = 0 
                event_type_priority_sum = 0

                for k in range(0, len(event_type_priority)):
                    event_type_priority_sum = event_type_priority_sum + event_type_priority[k]
               

                for i in range(0, len(pull_req_events_per_repo)):
                    pull_req_events_count_per_repo_sum = pull_req_events_count_per_repo_sum + pull_req_events_per_repo[i]

                rank = 0

                if pullrequests_count == 0 :

                    rank = pullrequests_count + pull_req_events_count_per_repo_sum  + (int(content_len) *2)

                else: 
                    rank = (pullrequests_count *2 ) + (pull_req_events_count_per_repo_sum + ((pull_req_events_count_per_repo_sum/pullrequests_count) * event_type_priority_sum)) + int(content_len)


                    




                list_codecommit.append((repo['repositoryId'],repo['repositoryName'],pullrequests_count, pull_req_events_count_per_repo_sum, content_len, account_id, rank ))
                pullrequests_per_repo.append(repo['repositoryName'])
                


            print("total count of repo " + str(len(list_codecommit)))
            print("count of pullreq per repo " + str(pullrequests_count))
            # print("count of pullreq events  per repo " + str(pull_req_events_count_per_repo_sum))


            
            if 'nextToken' in  response1.keys():
                next_token = response1['nextToken']
            if 'nextToken' in  response3.keys():
                next_token3 = response3['nextToken']               
            else:
                break
        print(list_codecommit)
        



    except Exception as e :
        print ( "Exception occured ")
        print(e)
        continue

print("here")
def myFunc(e):
    return e[6]
list_codecommit.sort(key=myFunc)
print(list_codecommit)
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          