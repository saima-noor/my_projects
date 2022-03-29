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
        pullrequests_per_repo = []
        conflicts_per_repo = []
        while True:
            response3 = {}
            response1 = codecommit_client.list_repositories(nextToken= next_token) if next_token else codecommit_client.list_repositories()
            print(response1['repositories'])                                                            
            for repo in response1['repositories']:

                 
                print(repo['repositoryName']) 
                next_token3 = None
          
                response3 = codecommit_client.list_pull_requests(repositoryName=repo['repositoryName'],nextToken= next_token3) if next_token3 else codecommit_client.list_pull_requests(repositoryName=repo['repositoryName'])
                print(response3)

                print(response3['pullRequestIds'])
                print("total count of pull requests for repo "  + repo['repositoryName'] + "  " + str(len(response3['pullRequestIds'])))
                pullrequests_count = len(response3['pullRequestIds'])
                pullreq_id = response3['pullRequestIds']



                for reqs in pullreq_id:
                
                    response5 = codecommit_client.describe_pull_request_events(pullRequestId= reqs)
                    # print(response4)

                    for events in response5['pullRequestEvents']:
                        if events['pullRequestEventType'] == 'PULL_REQUEST_CREATED':
                            print("here,,,,,,,,,,,,,,,,,,,")
                            print(events)

                            print(events['pullRequestCreatedEventMetadata']['repositoryName'])
                            response6 = codecommit_client.get_merge_conflicts(
                            repositoryName=events['pullRequestCreatedEventMetadata']['repositoryName'],
                            destinationCommitSpecifier=events['pullRequestCreatedEventMetadata']['destinationCommitId'],
                            sourceCommitSpecifier= events['pullRequestCreatedEventMetadata']['sourceCommitId'],
                            mergeOption= 'FAST_FORWARD_MERGE')

                            print(response6)

                            if response6['mergeable'] == True:
                                print("No conflict")
                            else:
                                print("conflict")
                                conflicts_per_repo.append("yes")

                conflicts_per_repo_sum = 0

                for i in range(0, len(conflicts_per_repo)):
                   conflicts_per_repo_sum = conflicts_per_repo_sum + conflicts_per_repo[i]

                print(conflicts_per_repo_sum)





                # list_codecommit.append((repo['repositoryName'],pullrequests_count ))
                # pullrequests_per_repo.append(repo['repositoryName'])


            # print("total count of repo " + str(len(list_codecommit)))
            # print("count of repo per region " + str(len(pullrequests_per_repo)))
            print(conflicts_per_repo_sum)
            
            if 'nextToken' in  response1.keys():
                next_token = response1['nextToken']
            if 'nextToken' in  response3.keys():
                next_token3 = response3['nextToken']               
            else:
                break
        # print(list_codecommit)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception as e  :
        print ( "Exception occured ")
        print(e)
        continue
                




