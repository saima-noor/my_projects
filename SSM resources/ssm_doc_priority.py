

import re
aut_docs = ['AWS-ASGEnterStandby', 'AWS-ASGExitStandby', 'AWS-AddOpsItemDedupStringToEventBridgeRule', 'AWS-AttachEBSVolume', 'AWS-AttachIAMToInstance', 
'AWS-BulkEditOpsItems', 'AWS-BulkResolveOpsItems', 'AWS-ChangeDDBRWCapacityMode', 'AWS-CloseSecurityGroup', 'AWS-ConfigureCloudTrailLogging', 
'AWS-ConfigureCloudWatchOnEC2Instance', 'AWS-ConfigureS3BucketLogging', 'AWS-ConfigureS3BucketVersioning', 'AWS-CopySnapshot', 
'AWS-CreateDSManagementInstance', 'AWS-CreateDynamoDbBackup', 'AWS-CreateEncryptedRdsSnapshot', 'AWS-CreateImage', 'AWS-CreateJiraIssue', 'AWS-CreateManagedLinuxInstance', 'AWS-CreateManagedLinuxInstanceWithApproval', 'AWS-CreateManagedWindowsInstance', 'AWS-CreateManagedWindowsInstanceWithApproval', 'AWS-CreateRdsSnapshot', 'AWS-CreateServiceNowIncident', 'AWS-CreateSnapshot', 'AWS-DeleteCloudFormationStack', 'AWS-DeleteCloudFormationStackWithApproval', 'AWS-DeleteDynamoDbBackup', 'AWS-DeleteDynamoDbTableBackups', 'AWS-DeleteEKSCluster', 'AWS-DeleteEbsVolumeSnapshots', 'AWS-DeleteIAMInlinePolicy', 'AWS-DeleteImage', 'AWS-DeleteSnapshot', 'AWS-DetachEBSVolume', 'AWS-DisableEventBridgeRule', 'AWS-DisableIncomingSSHOnPort22', 'AWS-DisablePublicAccessForSecurityGroup', 'AWS-DisableS3BucketPublicReadWrite', 'AWS-EnableCLBAccessLogs', 'AWS-EnableCWAlarm', 'AWS-EnableCloudTrail', 'AWS-EnableCloudTrailCloudWatchLogs', 'AWS-EnableCloudTrailKmsEncryption', 'AWS-EnableCloudTrailLogFileValidation', 'AWS-EnableExplorer', 'AWS-EnableS3BucketEncryption', 'AWS-EnableVPCFlowLogs', 'AWS-ExportOpsDataToS3', 'AWS-ExportPatchReportToS3', 'AWS-HelloWorld', 'AWS-InstallAmazonECSAgent', 'AWS-ModifyDynamoDBProvisionedCapacity', 'AWS-PatchAsgInstance', 'AWS-PatchInstanceWithRollback', 'AWS-PublishSNSNotification', 'AWS-RebootRdsInstance', 'AWS-ReleaseElasticIP', 'AWS-ResizeInstance', 'AWS-RestartEC2Instance', 'AWS-RestartEC2InstanceWithApproval', 'AWS-RestrictIncomingTraffic', 'AWS-RunCfnLint', 'AWS-RunPacker', 'AWS-SetRequiredTags', 'AWS-SetupInventory', 'AWS-SetupManagedInstance', 'AWS-SetupManagedRoleOnEc2Instance', 'AWS-StartEC2Instance', 'AWS-StartEC2InstanceWithApproval', 'AWS-StartRdsInstance', 'AWS-StartStopAuroraCluster', 'AWS-StopEC2Instance', 'AWS-StopEC2InstanceWithApproval', 'AWS-StopRdsInstance', 'AWS-TerminateEC2Instance', 'AWS-TerminateEC2InstanceWithApproval', 'AWS-UpdateAmazonECSAgent', 'AWS-UpdateCloudFormationStack', 'AWS-UpdateCloudFormationStackWithApproval', 'AWS-UpdateEKSManagedNodegroupVersion', 'AWS-UpdateLinuxAmi', 'AWS-UpdateWindowsAmi', 'AWSSupport-ActivateWindowsWithAmazonLicense', 'AWSSupport-CheckAndMountEFS', 'AWSSupport-CheckXenToNitroMigrationRequirements', 'AWSSupport-CollectEKSInstanceLogs', 'AWSSupport-CollectElasticBeanstalkLogs', 'AWSSupport-ConfigureDNSQueryLogging', 'AWSSupport-ConfigureEC2Metadata', 'AWSSupport-ConnectivityTroubleshooter', 'AWSSupport-CopyEC2Instance', 'AWSSupport-EnableVPCFlowLogs', 'AWSSupport-ExecuteEC2Rescue', 'AWSSupport-GrantPermissionsToIAMUser', 'AWSSupport-ListEC2Resources', 'AWSSupport-ManageRDPSettings', 'AWSSupport-ManageWindowsService', 'AWSSupport-MigrateEC2ClassicToVPC', 'AWSSupport-RecoverWorkSpace', 'AWSSupport-RecoverWorkSpaceWithApproval', 'AWSSupport-ResetAccess', 'AWSSupport-RestoreEC2InstanceFromSnapshot', 'AWSSupport-SendLogBundleToS3Bucket', 'AWSSupport-SetupConfig', 'AWSSupport-SetupIPMonitoringFromVPC', 'AWSSupport-ShareRDSSnapshot', 'AWSSupport-StartEC2RescueWorkflow', 'AWSSupport-TerminateIPMonitoringFromVPC', 'AWSSupport-TroubleshootCodeDeploy', 'AWSSupport-TroubleshootConnectivityToRDS', 'AWSSupport-TroubleshootDirectoryTrust', 'AWSSupport-TroubleshootLambdaInternetAccess', 'AWSSupport-TroubleshootLambdaS3Event', 'AWSSupport-TroubleshootManagedInstance', 'AWSSupport-TroubleshootRDP', 'AWSSupport-TroubleshootS3PublicRead', 'AWSSupport-TroubleshootSSH', 'AWSSupport-TroubleshootSUSERegistration', 'AWSSupport-UpgradeWindowsAWSDrivers', 'AWSEC2-CloneInstanceAndUpgradeSQLServer', 'AWSEC2-CloneInstanceAndUpgradeWindows', 'AWSEC2-CloneInstanceAndUpgradeWindows2019', 'AWSEC2-SQLServerDBRestore', 'AWSDocs-ClassicLoadBalancerSSMDocument', 'AWSDocs-Configure-SSL-TLS-AL', 'AWSDocs-Configure-SSL-TLS-AL2', 'AWSDocs-HostingAWordPressBlog-AL', 'AWSDocs-HostingAWordPressBlog-AL2', 'AWSDocs-InstallALAMPServer-AL', 'AWSDocs-InstallALAMPServer-AL2', 'AWSDocs-LambdaWithS3SSMDocument', 'AWSDocs-S3StaticWebsite', 'AWSDocs-S3StaticWebsiteCustomDomain', 'AWSDocs-ScaleLoadBalanced', 'AWSConfigRemediation-CancelKeyDeletion', 'AWSConfigRemediation-ConfigureCodeBuildProjectWithKMSCMK', 'AWSConfigRemediation-ConfigureLambdaFunctionXRayTracing', 'AWSConfigRemediation-ConfigureS3BucketPublicAccessBlock', 'AWSConfigRemediation-ConfigureS3PublicAccessBlock', 'AWSConfigRemediation-CreateCloudTrailMultiRegionTrail', 'AWSConfigRemediation-CreateGuardDutyDetector', 'AWSConfigRemediation-DeleteAPIGatewayStage', 'AWSConfigRemediation-DeleteAccessKeysFromCodeBuildProject', 'AWSConfigRemediation-DeleteDefaultVPCRoutes', 'AWSConfigRemediation-DeleteDynamoDbTable', 'AWSConfigRemediation-DeleteEgressOnlyInternetGateway', 'AWSConfigRemediation-DeleteElasticsearchDomain', 'AWSConfigRemediation-DeleteIAMRole', 'AWSConfigRemediation-DeleteIAMUser', 'AWSConfigRemediation-DeleteLambdaFunction', 'AWSConfigRemediation-DeleteRDSCluster', 'AWSConfigRemediation-DeleteRDSClusterSnapshot', 'AWSConfigRemediation-DeleteRDSInstance', 'AWSConfigRemediation-DeleteRDSInstanceSnapshot', 'AWSConfigRemediation-DeleteRedshiftCluster', 'AWSConfigRemediation-DeleteSecret', 'AWSConfigRemediation-DeleteUnusedEBSVolume', 'AWSConfigRemediation-DeleteUnusedENI', 'AWSConfigRemediation-DeleteUnusedIAMGroup', 'AWSConfigRemediation-DeleteUnusedIAMPolicy', 'AWSConfigRemediation-DeleteUnusedSecurityGroup', 'AWSConfigRemediation-DeleteUnusedVPCNetworkACL', 'AWSConfigRemediation-DeleteVPCFlowLog', 'AWSConfigRemediation-DetachAndDeleteInternetGateway', 'AWSConfigRemediation-DetachAndDeleteVirtualPrivateGateway', 'AWSConfigRemediation-DetachIAMPolicy', 'AWSConfigRemediation-DisablePublicAccessToRDSInstance', 'AWSConfigRemediation-DisablePublicAccessToRedshiftCluster', 'AWSConfigRemediation-DisableSubnetAutoAssignPublicIP', 'AWSConfigRemediation-DropInvalidHeadersForALB', 'AWSConfigRemediation-EnableAPIGatewayTracing', 'AWSConfigRemediation-EnableAccountAccessAnalyzer', 'AWSConfigRemediation-EnableAutoScalingGroupELBHealthCheck', 'AWSConfigRemediation-EnableBeanstalkEnvironmentNotifications', 'AWSConfigRemediation-EnableCLBCrossZoneLoadBalancing', 'AWSConfigRemediation-EnableCWLoggingForSessionManager', 'AWSConfigRemediation-EnableCloudFrontAccessLogs', 'AWSConfigRemediation-EnableCloudFrontDefaultRootObject', 'AWSConfigRemediation-EnableCloudFrontOriginAccessIdentity', 'AWSConfigRemediation-EnableCloudFrontOriginFailover', 'AWSConfigRemediation-EnableCloudFrontViewerPolicyHTTPS', 'AWSConfigRemediation-EnableCloudTrailEncryptionWithKMS', 'AWSConfigRemediation-EnableCloudTrailLogFileValidation', 'AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSCluster', 'AWSConfigRemediation-EnableCopyTagsToSnapshotOnRDSDBInstance', 'AWSConfigRemediation-EnableELBDeletionProtection', 'AWSConfigRemediation-EnableEbsEncryptionByDefault', 'AWSConfigRemediation-EnableElasticBeanstalkEnvironmentLogStreaming', 'AWSConfigRemediation-EnableEncryptionOnDynamoDbTable', 'AWSConfigRemediation-EnableEnhancedMonitoringOnRDSInstance', 'AWSConfigRemediation-EnableKeyRotation', 'AWSConfigRemediation-EnableLoggingForALBAndCLB', 'AWSConfigRemediation-EnableMinorVersionUpgradeOnRDSDBInstance', 'AWSConfigRemediation-EnableMultiAZOnRDSInstance', 'AWSConfigRemediation-EnableNLBCrossZoneLoadBalancing', 'AWSConfigRemediation-EnablePITRForDynamoDbTable', 'AWSConfigRemediation-EnablePerformanceInsightsOnRDSInstance', 'AWSConfigRemediation-EnableRDSClusterDeletionProtection', 'AWSConfigRemediation-EnableRDSInstanceBackup', 'AWSConfigRemediation-EnableRDSInstanceDeletionProtection', 'AWSConfigRemediation-EnableRedshiftClusterAuditLogging', 'AWSConfigRemediation-EnableRedshiftClusterAutomatedSnapshot', 'AWSConfigRemediation-EnableRedshiftClusterEncryption', 'AWSConfigRemediation-EnableRedshiftClusterEnhancedVPCRouting', 'AWSConfigRemediation-EnableSecurityHub', 'AWSConfigRemediation-EnableSystemsManagerSessionManagerAuditLogsToS3', 'AWSConfigRemediation-EnableVPCFlowLogsToCloudWatch', 'AWSConfigRemediation-EnableVPCFlowLogsToS3Bucket', 'AWSConfigRemediation-EnableWAFClassicLogging', 'AWSConfigRemediation-EnableWAFClassicRegionalLogging', 'AWSConfigRemediation-EnableWAFV2Logging', 'AWSConfigRemediation-EncryptLambdaEnvironmentVariablesWithCMK', 'AWSConfigRemediation-EncryptSNSTopic', 'AWSConfigRemediation-EnforceEC2InstanceIMDSv2', 'AWSConfigRemediation-EnforceHttpsOnEsDomain', 'AWSConfigRemediation-EnforceSSLOnlyConnectionsToRedshiftCluster', 'AWSConfigRemediation-ModifyEBSVolumeType', 'AWSConfigRemediation-ModifyRDSInstancePortNumber', 'AWSConfigRemediation-ModifyRedshiftClusterMaintenanceSettings', 'AWSConfigRemediation-ModifyRedshiftClusterNodeType', 'AWSConfigRemediation-MoveLambdaToVPC', 'AWSConfigRemediation-RemovePrincipalStarFromS3BucketPolicy', 'AWSConfigRemediation-RemoveUnrestrictedSourceIngressRules', 'AWSConfigRemediation-RemoveUserPolicies', 'AWSConfigRemediation-RemoveVPCDefaultSecurityGroupRules', 'AWSConfigRemediation-ReplaceIAMInlinePolicy', 'AWSConfigRemediation-RestrictBucketSSLRequestsOnly', 'AWSConfigRemediation-RevokeUnusedIAMUserCredentials', 'AWSConfigRemediation-RotateSecret', 'AWSConfigRemediation-SetIAMPasswordPolicy', 'AWSConfigRemediation-UpdateAPIGatewayMethodCaching', 'AWSConfigRemediation-UpdateElasticsearchDomainSecurityGroups', 'AWSConfigRemediation-UpdateXRayKMSKey', 'AWSSQLServer-Backup', 'AWSSQLServer-DBCC', 'AWSSQLServer-Index', 'AWSSQLServer-Restore', 'AWSIncidents-CriticalIncidentRunbookTemplate', 'AWSResilienceHub-BacktrackRdsSOP_2020-04-01', 'AWSResilienceHub-BlockSQSDeleteMessageTest_2021-03-09', 'AWSResilienceHub-BreakEFSSecurityGroupTest_2020-09-21', 
'AWSResilienceHub-BreakLambdaSecurityGroupTest_2020-09-21', 'AWSResilienceHub-BreakSQSQueuePolicyTest_2020-11-27', 
'AWSResilienceHub-ChangeEFSProvisionedThroughputSOP_2020-10-26', 'AWSResilienceHub-ChangeHttpWsApiGwThrottlingSettingsSOP_2020-10-26', 
'AWSResilienceHub-ChangeLambdaConcurrencyLimitSOP_2020-10-26', 'AWSResilienceHub-ChangeLambdaExecutionTimeLimitSOP_2020-10-26', 'AWSResilienceHub-ChangeLambdaMemorySizeSOP_2020-10-26', 'AWSResilienceHub-ChangeLambdaProvisionedConcurrencySOP_2020-10-26', 'AWSResilienceHub-ChangeRestApiGwQuotaLimitSOP_2020-10-26', 'AWSResilienceHub-ChangeRestApiGwThrottlingSettingsSOP_2020-10-26', 'AWSResilienceHub-CleanS3BucketUtil_2020-03-03', 'AWSResilienceHub-CopyDynamoDBTablePropertiesUtil_2020-04-01', 'AWSResilienceHub-CreateEFSBackupSOP_2020-10-26', 'AWSResilienceHub-CreateNewDocumentDBInstanceSOP_2020-09-21', 'AWSResilienceHub-ExceedRestApiGwQuotaTest_2020-09-21', 'AWSResilienceHub-FailoverRdsAuroraClusterTest_2020-04-01', 'AWSResilienceHub-FailoverRdsInstanceTest_2020-04-01', 'AWSResilienceHub-ForceDocumentDBDatabaseToBeInaccessibleTest_2020-09-21', 'AWSResilienceHub-ForceDynamoDBTableReadThrottlingTest_2020-09-21', 'AWSResilienceHub-ForceLambdaThrottlingTest_2020-10-26', 'AWSResilienceHub-ForceSQSCapacityFailureTest_2021-03-13', 'AWSResilienceHub-ForceSQSFifoQueueMaxReceiveFailureTest_2020-11-27', 'AWSResilienceHub-ForceSQSStandardQueueMaxReceiveFailureTest_2020-11-27', 'AWSResilienceHub-IncreaseVolumeSizeEbsSOP_2020-05-26', 'AWSResilienceHub-InjectCpuLoadInAsgTest_2021-09-22', 'AWSResilienceHub-InjectCpuLoadInEc2Test_2020-07-28', 'AWSResilienceHub-InjectMemoryLoadInAsgTest_2020-10-11', 'AWSResilienceHub-InjectMemoryLoadInEc2Test_2020-07-28', 'AWSResilienceHub-KillProcessInEc2Test_2021-10-22', 'AWSResilienceHub-KillStressOnHealthyInstances_2020-07-28', 'AWSResilienceHub-MoveSQSMessagesBetweenQueuesSOP_2021-03-11', 'AWSResilienceHub-PromoteDocumentDBReadReplicaSOP_2020-09-21', 'AWSResilienceHub-PromoteRdsReadReplicaSOP_2020-04-01', 'AWSResilienceHub-PurgeSQSQueueSOP_2021-03-11', 'AWSResilienceHub-RebootDocumentDBInstanceTest_2020-09-21', 'AWSResilienceHub-RebootEc2InstanceSOP_2020-05-20', 'AWSResilienceHub-RebootRdsInstanceTest_2020-04-01', 'AWSResilienceHub-RefreshInstancesInAsgTest_2020-07-23', 'AWSResilienceHub-RestoreDocumentDBClusterFromBackupSOP_2020-09-21', 'AWSResilienceHub-RestoreDocumentDBClusterFromPointInTimeSOP_2020-09-21', 'AWSResilienceHub-RestoreDynamoDBTableFromBackupSOP_2020-04-01', 'AWSResilienceHub-RestoreDynamoDBTableToPointInTimeSOP_2020-04-01', 'AWSResilienceHub-RestoreEFSBackupInAnotherRegionSOP_2020-10-26', 'AWSResilienceHub-RestoreFromBackupEbsSOP_2020-05-26', 'AWSResilienceHub-RestoreFromRdsBackupSOP_2020-04-01', 'AWSResilienceHub-RestoreS3BucketFromBackupSOP_2020-09-21', 'AWSResilienceHub-RestoreS3ObjectToPreviousVersionSOP_2020-09-21', 'AWSResilienceHub-ScaleDownDocumentDBClusterSOP_2020-09-21', 'AWSResilienceHub-ScaleOutAsgSOP_2020-07-01', 'AWSResilienceHub-ScaleUpAsgSOP_2020-07-01', 'AWSResilienceHub-ScaleUpDocumentDBClusterSOP_2020-09-21', 'AWSResilienceHub-ScaleUpEc2SOP_2020-05-20', 'AWSResilienceHub-SimulateAzOutageInAsgTest_2020-07-23', 'AWSResilienceHub-SimulateNatGwInternetUnavailableTest_2020-09-21', 'AWSResilienceHub-SimulateRestApiGwNetworkUnavailableTest_2020-09-21', 'AWSResilienceHub-SimulateS3ObjectsAccidentalDeleteTest_2020-04-01', 'AWSResilienceHub-SwitchLambdaVersionInAliasSOP_2020-10-26', 'AWSResilienceHub-TriggerHttpWsApiGwThrottlingTest_2020-09-21', 'AWSResilienceHub-TriggerRestApiGwThrottlingTest_2020-09-21', 'AWSResilienceHub-UpdateDynamoDBTableProvisionedCapacitySOP_2020-04-01', 'AWSResilienceHub-UpdateHttpWsApiGwVersionSOP_2020-10-26', 'AWSResilienceHub-UpdateRestApiGwVersionSOP_2020-10-26']

print(len(aut_docs))
automation_doc_count = len(aut_docs)



command_docs = ['AWS-ApplyAnsiblePlaybooks', 'AWS-ApplyChefRecipes', 'AWS-ApplyDSCMofs', 'AWS-ApplyPatchBaseline', 'AWS-ConfigureAWSPackage', 'AWS-ConfigureCloudWatch', 'AWS-ConfigureDocker', 'AWS-ConfigureKernelLivePatching', 'AWS-ConfigureWindowsUpdate', 'AWS-FindWindowsUpdates', 'AWS-InstallApplication', 'AWS-InstallMissingWindowsUpdates', 'AWS-InstallPowerShellModule', 'AWS-InstallSpecificWindowsUpdates', 'AWS-InstallWindowsUpdates', 'AWS-InstanceRebootWithHooks', 'AWS-JoinDirectoryServiceDomain', 'AWS-ListWindowsInventory', 'AWS-RefreshAssociation', 'AWS-RunAnsiblePlaybook', 'AWS-RunDockerAction', 'AWS-RunDocument', 'AWS-RunInspecChecks', 'AWS-RunPatchBaseline', 'AWS-RunPatchBaselineAssociation', 'AWS-RunPatchBaselineWithHooks', 'AWS-RunPowerShellScript', 'AWS-RunRemoteScript', 'AWS-RunSaltState', 'AWS-RunShellScript', 'AWS-UpdateEC2Config', 'AWS-UpdateSSMAgent', 'AmazonInspector-ManageAWSAgent', 'AmazonCloudWatch-ManageAgent', 'AmazonCloudWatch-MigrateCloudWatchAgent', 'AWSSupport-RunEC2RescueForWindowsTool', 'AWSSAP-InstallBackint', 'AWSEC2-ApplicationInsightsCloudwatchAgentInstallAndConfigure', 'AWSEC2-CheckPerformanceCounterSets', 'AWSEC2-ConfigureSTIG', 'AWSEC2-CreateVssSnapshot', 'AWSEC2-DetectWorkload', 'AWSEC2-ManageVssIO', 'AWSEC2-RunSysprep', 'AWSEC2Launch-RunMigration', 'AWSFleetManager-AddUsersToGroups', 'AWSFleetManager-CopyFileSystemItem', 'AWSFleetManager-CreateDirectory', 'AWSFleetManager-CreateGroup', 'AWSFleetManager-CreateUser', 'AWSFleetManager-CreateWindowsRegistryKey', 'AWSFleetManager-DeleteFileSystemItem', 'AWSFleetManager-DeleteGroup', 'AWSFleetManager-DeleteUser', 'AWSFleetManager-DeleteWindowsRegistryKey', 'AWSFleetManager-DeleteWindowsRegistryValue', 'AWSFleetManager-GetFileSystemContent', 'AWSFleetManager-GetGroups', 'AWSFleetManager-GetUsers', 'AWSFleetManager-GetWindowsEvents', 'AWSFleetManager-GetWindowsRegistryContent', 'AWSFleetManager-MoveFileSystemItem', 'AWSFleetManager-RemoveUsersFromGroups', 'AWSFleetManager-RenameFileSystemItem', 'AWSFleetManager-SetWindowsRegistryValue', 'AWSFleetManager-StartProcess', 'AWSFleetManager-TerminateProcess', 'AWSFIS-Run-CPU-Stress', 'AWSFIS-Run-IO-Stress', 'AWSFIS-Run-Kill-Process', 'AWSFIS-Run-Memory-Stress', 'AWSFIS-Run-Network-Blackhole-Port', 'AWSFIS-Run-Network-Latency', 'AWSFIS-Run-Network-Latency-Sources', 'AWSFIS-Run-Network-Packet-Loss', 'AWSFIS-Run-Network-Packet-Loss-Sources', 'AWSSSO-CreateSSOUser', 'AWSResilienceHub-KillStressCommand_2020-07-28']

print(len(command_docs))
comand_docs_count = len(command_docs)

policy_docs =["AWS-GatherSoftwareInventory"]


yes = []


all_docs_rank= []
def docs(listOfDocs):
    for i in listOfDocs:
        words = re.findall('[A-Z]*[^A-Z]*', i) 
        print(words)

        for k in words:
            if (k== "Run-" or k=="Run" or k=="Launch" or k=="Execute"):
                print(k)
                yes.append((i,0.090))
            elif (k==  "Configure" or k=="Setup" or k=="Encrypt"):
                # print(k)
                yes.append((i,0.080))
            elif (k== "Apply" or k=="Patch"):
                # print(k)
                yes.append((i,0.070))
            elif (k== "Install" or k=="Grant" or k=="Force" or k=="Enforce"):
                # print(k)
                yes.append((i,0.060))
            elif (k== "Find" or k=="Get" or k=="List" or k=="Detect" or k=="Check" or k=="Index" or k=="Recover" or k=="Collect" or k== "Gather"):
                # print(k)
                yes.append((i,0.050))
            elif (k== "Create" or k=="Start" or k=="Publish" or k=="Activate"  or k=="Simulate" or k=="Hosting"  or k=="Enable" or k=="Trigger"):
                # print(k)
                yes.append((i,0.040))
    
            elif (k== "Manage" or k=="Resolve" or k=="Troubleshoot" or k=="Troubleshooter"):
                # print(k)
                yes.append((i,0.030))
            elif (k== "Refresh" or k=="Reboot" or k=="Restart" or k=="Reset"  or k=="Failover" or k=="Clean"  or k=="Backup" or k=="Revoke" or k=="Restore"):
                # print(k)
                yes.append((i,0.020))
            elif (k== "Add" or k=="Copy" or k=="Move" or k=="Migrate" or k=="Attach" or k=="Send" or k=="Share" or k=="Inject"):
                # print(k)
                yes.append((i,0.016))
            elif (k== "Remove" or k=="Terminate" or k=="Delete" or k=="Close" or k=="Drop" or k=="Cancel" or k=="Stop" or k=="Restrict" or k=="Disable" or k=="Detach" or k=="Block" or k=="Break" or k=="Kill"  or k=="Purge"):
                # print(k)
                yes.append((i,0.013))   
            elif (k== "Set" or k=="Update" or k=="Custom" or k=="Rename" or k=="Edit" or k=="Change" or k=="Scale" or k=="Upgrade" or k=="Resize" or k=="Modify" or k=="Rotate" or k=="Backtrack" or k=="Exceed" or k=="Increase"  or k=="Promote" or k=="Switch"):
                # print(k)
                yes.append((i,0.019)) 
    return yes
all_docs_rank= docs(policy_docs) 
all_docs_rank= docs(command_docs)
all_docs_rank =docs(aut_docs)
print("here")
print(all_docs_rank) 
print(len(all_docs_rank))
def myFunc(w):
            
    return w[1]
all_docs_rank.sort(key=myFunc)
print(all_docs_rank)
print("Again")
abb= "AWS-RefreshAssociation"
abbb = "AWSConfigRemediation-EnforceEC2InstanceIMDSv2"
for all in all_docs_rank:
    if abb in all:
        print("Yay")
        doc_rank = all[1]
        print(type(doc_rank))
    # else:
    #     print("sad")
