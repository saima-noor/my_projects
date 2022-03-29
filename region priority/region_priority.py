import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-2', 'us-east-1', 'us-west-1', 'us-west-2']
resources = []


def codePipeline(reg, add):
    next_token_pipeline = None
    pipeline_client = boto3.client('codepipeline', region_name = reg )
    pipelines = []
    while True:
        response_pipeline = pipeline_client.list_pipelines(nextToken= next_token_pipeline) if next_token_pipeline else pipeline_client.list_pipelines()
        for res in response_pipeline['pipelines']:
            #print(res['name'])
            resources.append(res['name'])
            pipelines.append(res['name'])
            add.append(res['name'])
            #print(len(pipelines))

               
        # print("count resources ---- " + str(len(resources)))
        # print("count pipelines ---- " + str(len(pipelines)))
        #print(response['pipelines'])

        if 'NextToken' in  response_pipeline.keys():
            next_token_pipeline = response_pipeline['NextToken']
            # funcs_arn.append(i['FunctionArn'])
                    # print(funcs_arn)
        else:
            break
    print("count of pipelines for region: " + reg + " ---- " + str(len(pipelines)))

def codeBuild(reg, add):
    project_client = boto3.client('codebuild', region_name = reg)
    projects = []
    next_token_project = None
    while True:
        response_project = project_client.list_projects(nextToken= next_token_project) if next_token_project else project_client.list_projects()
        for i in response_project['projects']:
            #print(i)
            resources.append(i)
            projects.append(i)
            add.append(i)
            #print(len(projects))
            
                
        # print("count resources ---- " + str(len(resources)))
        # print("count projects ---- " + str(len(projects)))            

        if 'nextToken' in  response_project.keys():
            next_token_project = response_project['nextToken']
            # funcs_arn.append(i['FunctionArn'])
            # print(funcs_arn)
        else:
            break
    
    print("count of projects  for region: " + reg + " ---- " + str(len(projects)))



def cloudWatch(reg,  add):
    alarm_client = boto3.client('cloudwatch', region_name = reg)
    alarms = []
    next_token = None
    while True:
        response_alarm = alarm_client.describe_alarms(NextToken= next_token) if next_token else alarm_client.describe_alarms()
        for i in response_alarm['MetricAlarms']:
            #print(i['AlarmArn'])
            resources.append(i['AlarmArn'])
            alarms.append(i['AlarmArn'])
            add.append(i['AlarmArn'])
            #print(len(alarms))

        # print("count resources ---- " + str(len(resources)))
        # print("count alarms ---- " + str(len(alarms)))
        #print(response['pipelines'])

        if 'NextToken' in  response_alarm.keys():
            next_token = response_alarm['NextToken']
            # funcs_arn.append(i['FunctionArn'])
            # print(funcs_arn)
        else:
            break
    print("count of alarms  for region: " + reg + " ---- " + str(len(alarms)))


def cloudTrail(reg,  add):
    trail_client = boto3.client('cloudtrail', region_name = reg)
    trails = []
    next_token_trails = None
    while True:
        response_trails = trail_client.list_trails(NextToken= next_token_trails) if next_token_trails else trail_client.list_trails()
        for i in response_trails['Trails']:
            #print(i['TrailARN'])
            resources.append(i['TrailARN'])
            trails.append(i['TrailARN'])
            add.append(i['TrailARN'])
            #print(len(trails))

        # print("count resources ---- " + str(len(resources)))
        # print("count alarms ---- " + str(len(alarms)))
        #print(response['pipelines'])

        if 'NextToken' in  response_trails.keys():
            next_token_trails = response_trails['NextToken']
            # funcs_arn.append(i['FunctionArn'])
            # print(funcs_arn)
        else:
            break
    print("count of trails  for region: " + reg + " ---- " + str(len(trails)))



def cloudFormation(reg,  add):
    stack_client = boto3.client('cloudformation', region_name = reg)
    stacks = []
    next_token_stacks = None
    while True:
        response_stacks = stack_client.list_stacks(NextToken= next_token_stacks) if next_token_stacks else stack_client.list_stacks()
        for i in response_stacks['StackSummaries']:
            #print(i['StackId'])
            resources.append(i['StackId'])
            stacks.append(i['StackId'])
            add.append(i['StackId'])
            #print(len(stacks))

        # print("count resources ---- " + str(len(resources)))
        # print("count alarms ---- " + str(len(alarms)))
        #print(response['pipelines'])

        if 'NextToken' in  response_stacks.keys():
            next_token_stacks = response_stacks['NextToken']
            # funcs_arn.append(i['FunctionArn'])
            # print(funcs_arn)
        else:
            break
    print("count of stacks  for region: " + reg + " ---- " + str(len(stacks)))


def lambda_f(reg, add):
    function_client = boto3.client('lambda', region_name = reg)
    functions = []
    next_marker  = None
    while True:
        response_functions = function_client.list_functions(Marker = next_marker) if next_marker else function_client.list_functions()
        for i in response_functions['Functions']:
            #print(i['FunctionArn'])
            resources.append(i['FunctionArn'])
            functions.append(i['FunctionArn'])
            add.append(i['FunctionArn'])
            #(len(functions))

        # print("count resources ---- " + str(len(resources)))
        # print("count alarms ---- " + str(len(alarms)))
        #print(response['pipelines'])

        if 'NextMarker' in  response_functions.keys():
            next_marker = response_functions['NextMarker']
            # funcs_arn.append(i['FunctionArn'])
            # print(funcs_arn)
        else:
            break
    print("count of functions  for region: " + reg + " ---- " + str(len(functions)))



list_reg =[]
for i in regions:
    try:
        resources_per_region = []
        print("..................................................................................................")
        print("region --- " + i)
        print("..................................................................................................")
        print("Here are all the codepipeline pipelines from "+ i +" region")
        
        codePipeline(i,resources_per_region )

        print("Here are all the codeBuild pojects from "+ i +" region")

        codeBuild(i, resources_per_region)

        print("Here are all the cloudWatch alarms from "+ i +" region")

        cloudWatch(i, resources_per_region)

        print("Here are all the cloudTrail trails from "+ i +" region")

        cloudTrail(i, resources_per_region)

        print("Here are all the cloudFormation stacks from "+ i +" region")

        cloudFormation(i, resources_per_region)

        print("Here are all the Lambda functions from "+ i +" region")

        lambda_f(i, resources_per_region)


        list_reg.append((i, len(resources_per_region)))

        print("count of all resources for region: " + i +  " ---- " + str(len(resources_per_region)))
        print("total count of  resources till now of all regions ---- " + str(len(resources)))


        
        


    except Exception :
        print ( "Exception occured ")
        list_reg.append((i, 0))
        print(list_reg)
        continue

print("Final count of all resources for all services and regions ---- " + str(len(resources)))
print(list_reg)


def myFunc(e):
  return e[1] 


list_reg.sort(key=myFunc)
print(list_reg)

sorted_regions = [item[0] for item in list_reg]
sorted_resource_freq = [item[1] for item in list_reg]
print(sorted_regions)
region_count = len(sorted_regions)

rank=0
index= 1

region_priority_list = []
for list in list_reg:
    print(list[0], list[1], rank)
    region_priority_list.append((list[0], list[1], rank))
    rank = rank + 1 if sorted_resource_freq[index] != sorted_resource_freq[index-1] else rank 
    index = index + 1 if index< len(sorted_resource_freq)- 1 else index

print(region_priority_list)

    





                




