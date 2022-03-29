from urllib import response
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
        auto_client = boto3.client('autoscaling',region_name = j)
        elb_client = boto3.client('elb',region_name = j)
        ec2_client = boto3.client('ec2',region_name = j)
        
        next_token = None
        next_token2 = None
        next_token3 = None
        marker = None
       
        while True:
            response3 = {}
            response4 = {}
            response5 = {}
            response1 = ebs_client.describe_environments(NextToken= next_token) if next_token else ebs_client.describe_environments()
            print(response1['Environments'])                                                            
            for env in response1['Environments']:
                
                
                print(env['EnvironmentName']) 
                print(env['ApplicationName']) 

                response2 = ebs_client.describe_environment_resources(EnvironmentId=env['EnvironmentId'],EnvironmentName=env['EnvironmentName'])

                print(response2)
                print(len(response2['EnvironmentResources']['AutoScalingGroups']))
                print(len(response2['EnvironmentResources']['Instances']))
                print(len(response2['EnvironmentResources']['LaunchConfigurations']))
                print(len(response2['EnvironmentResources']['LaunchTemplates']))
                print(len(response2['EnvironmentResources']['LoadBalancers']))
                print(len(response2['EnvironmentResources']['Triggers']))
                print(len(response2['EnvironmentResources']['Queues']))

                auto_scaling_groups = len(response2['EnvironmentResources']['AutoScalingGroups'])
                instances = len(response2['EnvironmentResources']['Instances'])
                launch_configurations = len(response2['EnvironmentResources']['LaunchConfigurations'])
                launch_templates = len(response2['EnvironmentResources']['LaunchTemplates'])
                load_balancers = len(response2['EnvironmentResources']['LoadBalancers'])
                triggers = len(response2['EnvironmentResources']['Triggers'])
                queues =len(response2['EnvironmentResources']['Queues'])






                total_resources = auto_scaling_groups + instances + launch_configurations + launch_templates + load_balancers + triggers + queues

                # print("............................")
                if auto_scaling_groups != 0:
                    for res in response2['EnvironmentResources']['AutoScalingGroups']:
                        print(res['Name'])
                        try:
                            response3 = auto_client.describe_auto_scaling_groups( AutoScalingGroupNames = [res['Name']], NextToken= next_token2) if next_token2 else auto_client.describe_auto_scaling_groups( AutoScalingGroupNames = [res['Name']])
                            print(response3['AutoScalingGroups'])                                                            
                            for autoscalegrp in response3['AutoScalingGroups']:
                                
                                #AutoScalingGroupNames= ['awseb-e-aq3frxmmmv-stack-AWSEBAutoScalingGroup-VQQBMVPVQ1AV']
                                print(autoscalegrp['AutoScalingGroupName']) 
                                print(autoscalegrp['AutoScalingGroupARN'])
                        except Exception as e1 :
                            print ( "Exception occured ")
                            print(e1)
                            continue

                if instances != 0:
                    for res1 in response2['EnvironmentResources']['Instances']:
                        print(res1['Id'])
                        try:
                            response4 = ec2_client.describe_instances( InstanceIds = [res1['Id']], NextToken= next_token3) if next_token3 else ec2_client.describe_instances( InstanceIds = [res1['Id']])
                            print(response4['Reservations'])                                                            
                            for ins in response4['Reservations']:
                                
                                #AutoScalingGroupNames= ['awseb-e-aq3frxmmmv-stack-AWSEBAutoScalingGroup-VQQBMVPVQ1AV']
                                print(ins['Instances']) 
                                print(ins['Groups'])
                        except Exception as e2 :
                            print ( "Exception occured ")
                            print(e2)
                            continue



                if load_balancers != 0:
                    for res2 in response2['EnvironmentResources']['LoadBalancers']:
                        print(res2['Name'])
                        try:

                            response5 =  elb_client.describe_load_balancers( LoadBalancerNames = [res2['Name']], Marker= marker) if marker else elb_client.describe_load_balancers(LoadBalancerNames = [res2['Name']])
                            print(response5['LoadBalancerDescriptions'])
                            for lb in response5['LoadBalancerDescriptions']:
                                print(lb['LoadBalancerName'])
                        except Exception as p :
                            print ( "Exception occured ")
                            print(p)
                            continue

                print(total_resources)


                rank=  (auto_scaling_groups * (auto_scaling_groups/total_resources) * 3 )+ (instances * (instances/total_resources) * 7 )+ (launch_configurations * (launch_configurations/total_resources) * 2)+ (launch_templates * (launch_templates/total_resources) * 5 )+ (load_balancers * (load_balancers/total_resources) * 6)+ (triggers * (triggers/total_resources) * 1 ) + (queues * (queues/total_resources) * 4)

                list_environments.append((env['EnvironmentName'], env['EnvironmentId'],total_resources, round(rank, 4)))
               

                
                         


            print(" total count of environtments " + str(len(list_environments)))
            # print("count per region " + str(len(repo_per_region)))

            
            if 'NextToken' in  response1.keys():
                next_token = response1['NextToken']
            if 'NextToken' in  response3.keys():
                next_token2 = response3['NextToken'] 
            if 'NextToken' in  response4.keys():
                next_token3 = response4['NextToken']      
            if 'Marker' in  response5.keys():
                marker = response5['NextMarker']           
            else:
                break
        print(list_environments)
        
        # print("here")
        # def myFunc(e):
        #     return e[4]
        # list_ssm.sort(key=myFunc)
        # print(list_ssm)


    except Exception as e :
        print ( "Exception occured ")
        print(e)
        continue
                




