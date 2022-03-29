import boto3
import json
# import time
# from inspect import getmembers
# from optparse import OptionParser
# import sys
# import os
# from botocore.config import Config
import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the lambda resource from "+ j +" region")
        print("..................................................................................................")
        lambda_client = boto3.client('lambda', region_name = j )

        funcs_arn = []
        #funcss = []
        next_marker = None

        while True:
            response_list_function =  lambda_client.list_functions(Marker= next_marker) if next_marker else lambda_client.list_functions()

            for i in response_list_function['Functions']:
                #print(i)
                print(i['FunctionArn'])
                #funcs_arn.append(i['FunctionArn'])
                funcs_arn.append(i['FunctionArn'])
                #print(funcs_arn)
        
                arn = i['FunctionArn']
                #print(len(i['FunctionArn']))
                #print(arn)
        


       
                elements = arn.split(':', 6)
                result = {
                    'arn': elements[0],
                    'partition': elements[1],
                    'service': elements[2],
                    'region': elements[3],
                    'account': elements[4],
                    'resource_type': elements[5],
                    'resource_name': elements[6]
                    }
                    #print(elements)

                regions = []

                #print(result['region'])
                # regions.append(result['region'])
                # print(len(regions))


            #print(funcs_arn)
            print(len(funcs_arn))
            if 'NextMarker' in  response_list_function.keys():
                next_marker = response_list_function['NextMarker']
                # funcs_arn.append(i['FunctionArn'])
                # print(funcs_arn)
            else:
                break
                funcs_arn.append(i['FunctionArn'])
    
    except botocore.exceptions.ClientError:
        print("exception error" )
        # print(len(resourse_arn))
        #print(funcs_arn)
        # print(len(funcs_arn))