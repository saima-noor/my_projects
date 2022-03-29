import boto3
import json

region_client = boto3.client('ec2')

region_res = region_client.describe_regions(
    #Filters=[
        #{
           # 'Name': 'string',
            #'Values': [
                #'string',
            #]
       # },
    #],
    #RegionNames=[
       # 'string',
    #],
    #DryRun=True,
    AllRegions=True
)

print(region_res)

regions=[]

for i in region_res["Regions"]:
    #for j in i["RegionName"]:
        #print(i["RegionName"])
    regions.append(i["RegionName"])
            
print(regions)