import boto3
import json

import botocore
# import operator
list_ssm = []
regions=['af-south-1', 'eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-south-1', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2', 'me-south-1', 'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-east-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']
for j in regions:
    try:
        print("Here are all the ssm automation_executions from "+ j +" region")
        print("..................................................................................................")


        automation_stepexecutions_client = boto3.client('ssm', region_name = j )
        ssm_client = boto3.client('ssm', region_name = j )
        
        next_token = None
        next_token2 = None
        while True:
            response2 = ssm_client.describe_automation_executions(
                                                                        NextToken= next_token
                                                                    ) if next_token else ssm_client.describe_automation_executions()
            print(response2['AutomationExecutionMetadataList'])                                                            
            for autom in response2['AutomationExecutionMetadataList']:
                
                
                print(autom['AutomationExecutionId']) 
                automation_execution_id = []
                automation_execution_id.append(autom['AutomationExecutionId'])
                status_var2 = autom['AutomationExecutionStatus']
                # print(status_var)
                rank2 = 0                

                for aut in automation_execution_id:
                    print("for automation id  " + str(aut))
                    step_list_ssm = []
                    failed = []
                    pending = []


                    response3 = automation_stepexecutions_client.describe_automation_step_executions(AutomationExecutionId= aut,
                                                                                NextToken= next_token2
                                                                            ) if next_token2 else automation_stepexecutions_client.describe_automation_step_executions(AutomationExecutionId=aut,)
                    print(response3['StepExecutions']) 
                    secs = []                                                           
                    for step in response3['StepExecutions']:
                        
                        
                        print(step['StepName']) 

                        status_var3 = step['StepStatus']
                        # print(status_var)
                        rank2 = 0
                        if status_var3 == "Failed":
                            failed.append((step['StepName'],step['StepStatus']))
                        if status_var3 == "Pending":
                            pending.append((step['StepName'],step['StepStatus']))
                        

                        step_list_ssm.append((step['StepName'], step['Action'] ,step['StepExecutionId'],step['StepStatus'])) 
                        #step['ExecutionStartTime'],step['ExecutionEndTime']

                        step_action = step['Action']

                        if step_action == "aws:executeScript":
                            print(step['ExecutionStartTime'])
                            print(step['ExecutionEndTime'])
                            diff = step['ExecutionEndTime'] - step['ExecutionStartTime']
                            print(diff)
                            diff= str(diff)
                            # get_program_hours = diff.strftime('%H')
                            # get_program_minutes = diff.strftime('%M')
                            # get_program_hours_int = diff.hour
                            # get_program_minutes_int = diff.minute
                            # get_program_seconds_int = diff.second
                            elements = diff.split(':', 2)
                            result = {
                                'hour': int(elements[0]),
                                'minute': int(elements[1]),
                                'second': float(elements[2])
                            }  
                            print(result['hour']) 
                            print(result['minute']) 
                            print(result['second']) 

                            seconds = result['hour'] * 3600 + result['minute'] * 60 + result['second']

                            print(seconds)
                            secs.append(seconds)

                            # print(get_program_minutes)  
                            # print(get_program_seconds_int)   
                        else:
                            seconds = 0 
                            secs.append(seconds)                 


                        print("count of steps  " + str(len(step_list_ssm)))
                        # print("count of failed steps  " + str(len(failed)))
                        # print("count of pending steps " + str(len(pending)))
                    
                    for s in range(0, len(secs)):
                        
                        total = total + secs[s]
                    
                    print("step list of an automation ........................................................................")
                    print(step_list_ssm)
                    steps = len(step_list_ssm) 
                    ratio2 = (len(failed) + len(pending))/(len(step_list_ssm))
                    rank2 = rank2 + ratio2 
                    # rank = rank + (ratio *(len(failed) + len(pending)))
                    #if the pending and failure steps are high then the ratio is high and thus the rank/priority will increase



                if status_var2 == "Success":
                    rank2 = rank2 + (1*4) #intuitive rank is 4 for automations among the resource types
                if status_var2 == "Failed":
                    rank2 = rank2 + (1*4) + 5 #5 is added becuase there 5 resource types considered for SSM

                list_ssm.append((autom['AutomationExecutionId'], "Automation Execution" ,autom['DocumentName'],autom['AutomationExecutionStatus'], rank2))
            
            print("count of automations " + str(len(list_ssm)))

        
                    
                            
            if 'NextToken' in  response3.keys():
                next_token2 = response3['NextToken']
            
            # else:
            #     break

            

            
            if 'NextToken' in  response2.keys():
                next_token = response2['NextToken']
                
            else:
                break
                

        print(list_ssm)
        # print(step_list_ssm)
        print("Sorted list ---------------")
        def myFunc(e):
            
            return e[4]
        list_ssm.sort(key=myFunc)
        print(list_ssm)
        # print(range(len(list_ssm)))
        # print("here.............................................")

        # for leng in range(len(list_ssm)):
        #     print(list_ssm[leng])

        #     print(list_ssm[leng+1]) if leng < len(list_ssm) else print("end")
        # #     if list_ssm[len][4] == list_ssm[len+1][4]:
        # #         print("same")
        # #     else:
        # #         print("not same")  


    except Exception  as e:
        print ( "Exception occured ")
        print(e)
        continue
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          