from urllib import response
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
        branches_per_repo = []
        while True:
            response2 = {}
            response1 = codecommit_client.list_repositories(nextToken= next_token) if next_token else codecommit_client.list_repositories()
            print(response1['repositories'])                                                            
            for repo in response1['repositories']:
                 
                print(repo['repositoryName']) 
                next_token2 =None
          
                response2 = codecommit_client.list_branches(repositoryName=repo['repositoryName'],nextToken= next_token2) if next_token2 else codecommit_client.list_branches(repositoryName=repo['repositoryName'])

                print(response2['branches'])
                print("total count of branches for repo "  + repo['repositoryName'] + "  " + str(len(response2['branches'])))
                branches_count = len(response2['branches'])
                
              

                list_codecommit.append((repo['repositoryName'],branches_count ))
                branches_per_repo.append(repo['repositoryName'])

                for branches in response2['branches']:
                    response3 = codecommit_client.get_branch(repositoryName= repo['repositoryName'], branchName = branches)
                    print(response3['commitId'])

                


            print("total count of repo " + str(len(list_codecommit)))
            print("count of repo per region " + str(len(branches_per_repo)))

            
            if 'nextToken' in  response1.keys():
                next_token = response1['nextToken']
            if 'nextToken' in  response2.keys():
                next_token2 = response2['nextToken']               
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
                




