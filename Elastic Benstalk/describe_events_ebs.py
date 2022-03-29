import boto3
import json

import botocore
# import operator
list_environments = []

regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        ebs_client = boto3.client('elasticbeanstalk',region_name = j)
        
        next_token = None
        next_token2 = None
       
        while True:
            response5 = {}
            response1 = ebs_client.describe_environments(NextToken= next_token) if next_token else ebs_client.describe_environments()
            print(response1['Environments'])
            info = []  
            trace = []
            debug = []
            warn = []
            error = []
            fatal= []                                                          
            for env in response1['Environments']:
                
                
                print(env['EnvironmentName']) 
                print(env['ApplicationName']) 

                response5 = ebs_client.describe_events(ApplicationName=env['ApplicationName'], NextToken= next_token2) if next_token2 else ebs_client.describe_events(ApplicationName=env['ApplicationName'])

                print(response5['Events'])
                print(len(response5['Events']))
                total_event_count = len(response5['Events'])

                for event in response5['Events']:
                    print(event['Severity'])
                    if event['Severity'] == "INFO":
                        info.append(event['Severity'])
                    if event['Severity'] == "TRACE":
                        trace.append(event['Severity'])
                    if event['Severity'] == "WARN":
                        warn.append(event['Severity'])
                    if event['Severity'] == "ERROR":
                        error.append(event['Severity'])      
                    if event['Severity'] == "FATAL":
                        fatal.append(event['Severity'])
                    if event['Severity'] == "DEBUG":
                        debug.append(event['Severity'])                 

                print(len(info))       
                print(len(trace))
                print(len(debug))
                print(len(warn))
                print(len(error))
                print(len(fatal))

                events_with_info = len(info) #green
                events_with_debug = len(debug) #grey
                events_with_trace = len(trace) #grey
                events_with_warn = len(warn) #yellow
                events_with_error = len(error) # yellow
                events_with_fatal = len(fatal) #red

                


            
            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
            if 'NextToken' in  response5.keys():
                next_token2 = response5['NextToken']               
            else:
                break
        # print(list_environments)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception as e :
        print ( "Exception occured ")
        print(e)
        continue
                




