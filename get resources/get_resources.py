import boto3
import json
import time
from inspect import getmembers
from optparse import OptionParser
import sys
import os
from botocore.config import Config
import botocore


import boto3

region_client = boto3.client('ec2')

region_res = region_client.describe_regions(
   
    AllRegions=True
)

#print(region_res)

regions=[]

for i in region_res["Regions"]:
    #for j in i["RegionName"]:
        #print(i["RegionName"])
    regions.append(i["RegionName"])
    #region = i["RegionName"]
    #print(type(regions))

print(regions)
# All the region except Bahrain(me-south-1). If you have that region enabled, feel free to add that below.
# regions=['eu-west-3' ,'eu-west-2' ,'eu-west-1' ,'ap-northeast-3' , 'ap-northeast-2','ap-northeast-1', 'sa-east-1', 'ca-central-1', 'af-south-1','ap-southeast-1',  'ap-southeast-2',  'eu-central-1', 'us-east-1',  'us-east-2', 'us-west-1', 'us-west-2','sa-east-1','eu-north-1','ap-south-1', 'ap-east-1'
# ]
print(len(regions))
#def get_reg:
for i in regions:
    try:
        print("Here are all the resource from "+ i+" region")
        #my_config = Config(region_name = i)
        #print(i)
        client_res = boto3.client('resourcegroupstaggingapi', region_name = i )
        #print(client_res)
        print(i)
        print("......................................................................................................................................")
        #print("From the resources arn for region " + i + " we get")
        Resources = client_res.get_resources(
            #TagsPerPage=500,
            ResourceTypeFilters=[
                #"lambda:function"
                # "cloudformation:stack",
                # "cloudwatch:alarm",
                # "codepipeline:pipeline"
                # "cloudtrail:trail",
                "ssm:managedinstanceinventory"
                # "codebuild:project"
            ]
        )
    #Resources = paginator.paginate()
        print(Resources)



        resourse_arn=[]

        for j in Resources["ResourceTagMappingList"]:
            #print(i['ResourceARN'])
            resourse_arn.append(j['ResourceARN'])
            arn = j['ResourceARN']
            print(len(resourse_arn))
        


       
            elements = arn.split(':', 5)
            result = {
                'arn': elements[0],
                'partition': elements[1],
                'service': elements[2],
                'region': elements[3],
                'account': elements[4],
                'resource': elements[5],
                'resource_type': None
            }
            #print(elements)

            #regions = []

            #print(result['region'])
            if '/' in result['resource']:
                result['resource_type'], result['resource'] = result['resource'].split('/',1)
            elif ':' in result['resource']:
                result['resource_type'], result['resource'] = result['resource'].split(':',1)
        
            # regions.append(result['region'])
            # print(regions)
            # print(len(regions))
            # print(result['region'])
            # print(result['service'])
            # print(result['resource_type'])
            # print(result['resource'])

        #print(len(resourse_arn))
    
    except botocore.exceptions.ClientError:
        print("exception error" )
        # print(len(resourse_arn))
    
    # for Listofallresources in Resources:
    #     Mapping=Listofallresources['ResourceTagMappingList']
    #     for resourcelist in Mapping:
    #         print(resourcelist['ResourceARN'])
    #     print("\n")
       