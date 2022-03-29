import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the codeBuild Projects from "+ j +" region")
        print("..................................................................................................")


        project_client = boto3.client('codebuild', region_name = j)
        projects = []
        next_token = None
        while True:
            response = project_client.list_projects(nextToken= next_token) if next_token else project_client.list_projects()
            for i in response['projects']:
                print(i)
                projects.append(i)
                

                
            print("count ---- " + str(len(projects)))
            

            if 'nextToken' in  response.keys():
                next_token = response['nextToken']
                # funcs_arn.append(i['FunctionArn'])
                # print(funcs_arn)
            else:
                break

    except botocore.exceptions.ClientError:
        print("exception error" )
                




