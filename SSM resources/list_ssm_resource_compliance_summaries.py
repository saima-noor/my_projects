import boto3
import json

import botocore
# import operator
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm resource_compliance_summaries from "+ j +" region")
        print("..................................................................................................")


        ssm_client = boto3.client('ssm', region_name = j )
       

        list_ssm = []
        next_token = None
        while True:
            response4 = ssm_client.list_resource_compliance_summaries(
                                                                        NextToken= next_token
                                                                    ) if next_token else ssm_client.list_resource_compliance_summaries()
            
            print(response4['ResourceComplianceSummaryItems'])
            for comp in response4['ResourceComplianceSummaryItems']:

                status_var4 = comp['Status']
                Compliance_type = comp['ComplianceType']
             
                rank4 = 0
                compliant_count = comp['CompliantSummary']['CompliantCount']
                non_compliant_count = comp['NonCompliantSummary']['NonCompliantCount']

                ratio4 = non_compliant_count/( compliant_count+ non_compliant_count)
                if (status_var4 == "COMPLIANT" and Compliance_type == "Association") :
                    rank4 = 1*2 +ratio4
                if (status_var4 == "COMPLIANT" and Compliance_type == "Patch") :
                    rank4 = 1*3   +ratio4            
                if (status_var4 == "NON_COMPLIANT" and Compliance_type == "Association") :
                    rank4 = (1*2) + 5 +ratio4
                if (status_var4 == "NON_COMPLIANT" and Compliance_type == "Patch") :
                    rank4 = (1*3)+ 5 +ratio4



                
                list_ssm.append((comp['ResourceId'],comp['ResourceType'],comp['ComplianceType'],comp['Status'], rank4))



                     


        


            
            
            if 'NextToken' in  response4.keys():
                next_token = response4['NextToken']
                
            else:
                break

        print(list_ssm)
        print("here")
        def myFunc(e):
            return e[4]
        list_ssm.sort(key=myFunc)
        print(list_ssm)

    except Exception as e:
        print ( "Exception occured ")
        print(e)
        continue
                

        


