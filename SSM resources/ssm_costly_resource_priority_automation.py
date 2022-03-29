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
            response3 = {}
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
                    # failed = []
                    # pending = []


                    response3 = automation_stepexecutions_client.describe_automation_step_executions(AutomationExecutionId= aut,
                                                                                NextToken= next_token2
                                                                            ) if next_token2 else automation_stepexecutions_client.describe_automation_step_executions(AutomationExecutionId=aut,)
                    print(response3['StepExecutions']) 
                    execution_time_in_secs = [] 
                    step_count_with_scriptexecute = []                                                          
                    for step in response3['StepExecutions']:
                        
                        
                        print(step['StepName']) 

                        status_var3 = step['StepStatus']
                        # print(status_var)
                        rank2 = 2 # since automation has costing priority
                        # if status_var3 == "Failed":
                        #     failed.append((step['StepName'],step['StepStatus']))
                        # if status_var3 == "Pending":
                        #     pending.append((step['StepName'],step['StepStatus']))
                        

                        step_list_ssm.append((step['StepName'], step['Action'] ,step['StepExecutionId'],step['StepStatus'])) 
                        #step['ExecutionStartTime'],step['ExecutionEndTime']

                        step_action = step['Action']

                        if step_action == "aws:executeScript":
                            print(step['ExecutionStartTime'])
                            print(step['ExecutionEndTime'])
                            diff = step['ExecutionEndTime'] - step['ExecutionStartTime']
                            print(diff)
                            diff= str(diff)
                      
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
                            stepcount =1

                            print(seconds)
                            execution_time_in_secs.append(seconds)
                            step_count_with_scriptexecute.append(stepcount)

                        else:
                            seconds = 0 
                            stepcount =0
                            execution_time_in_secs.append(seconds)
                            step_count_with_scriptexecute.append(stepcount)



                        print("count of steps  " + str(len(step_list_ssm)))
                        # print("count of failed steps  " + str(len(failed)))
                        # print("count of pending steps " + str(len(pending)))
                    print(step_count_with_scriptexecute)
                    print(execution_time_in_secs)
                    
                    totalsecs = 0
                    totalsteps_withscript = 0
                    for s in range(0, len(execution_time_in_secs)):
                        
                        totalsecs = totalsecs + execution_time_in_secs[s]
                    for c in range(0, len(step_count_with_scriptexecute)):
                        
                        totalsteps_withscript = totalsteps_withscript + step_count_with_scriptexecute[c]   


                    print("step list of an automation ........................................................................")
                    # print(step_list_ssm)
                    totalsteps = len(step_list_ssm) 

                    step_rank = (totalsteps* 0.10000) + (totalsteps_withscript * 0.01000) + (totalsecs * 0.0000100)
                    print(step_rank)
                    step_rank = round(step_rank,6)
                    print(step_rank)
                    rank2 = rank2 + step_rank
         

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
  

    except Exception  as e:
        print ( "Exception occured ")
        print(e)
        continue
                




# 'Pending'|'InProgress'|'Waiting'|'Success'|'TimedOut'|'Cancelling'|'Cancelled'|'Failed'|'PendingApproval'|'Approved'|'Rejected'|'Scheduled'|'RunbookInProgress'|'PendingChangeCalendarOverride'|'ChangeCalendarOverrideApproved'|'ChangeCalendarOverrideRejected'|'CompletedWithSuccess'|'CompletedWithFailure',
          