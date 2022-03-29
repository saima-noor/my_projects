import boto3

count_resource_client =  boto3.client('config')

resource_type_list = ['AWS::SSM::FileData'] 
#'AWS::Lambda::Function','AWS::CloudTrail::Trail','AWS::CloudWatch::Alarm', 'AWS::CloudFormation::Stack',  'AWS::CodeBuild::Project','AWS::CodePipeline::Pipeline'  ,
#'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::SSM::FileData'|'AWS::SSM::ManagedInstanceInventory'
for i in resource_type_list:
    response = count_resource_client.get_aggregate_discovered_resource_counts(
        ConfigurationAggregatorName='aws-controltower-ConfigAggregatorForOrganizations',
        Filters={
            'ResourceType': i,
        #     #'ResourceType': 'AWS::EC2::CustomerGateway'|'AWS::EC2::EIP'|'AWS::EC2::Host'|'AWS::EC2::Instance'|'AWS::EC2::InternetGateway'|'AWS::EC2::NetworkAcl'|'AWS::EC2::NetworkInterface'|'AWS::EC2::RouteTable'|'AWS::EC2::SecurityGroup'|'AWS::EC2::Subnet'|'AWS::CloudTrail::Trail'|'AWS::EC2::Volume'|'AWS::EC2::VPC'|'AWS::EC2::VPNConnection'|'AWS::EC2::VPNGateway'|'AWS::EC2::RegisteredHAInstance'|'AWS::EC2::NatGateway'|'AWS::EC2::EgressOnlyInternetGateway'|'AWS::EC2::VPCEndpoint'|'AWS::EC2::VPCEndpointService'|'AWS::EC2::FlowLog'|'AWS::EC2::VPCPeeringConnection'|'AWS::Elasticsearch::Domain'|'AWS::IAM::Group'|'AWS::IAM::Policy'|'AWS::IAM::Role'|'AWS::IAM::User'|'AWS::ElasticLoadBalancingV2::LoadBalancer'|'AWS::ACM::Certificate'|'AWS::RDS::DBInstance'|'AWS::RDS::DBSubnetGroup'|'AWS::RDS::DBSecurityGroup'|'AWS::RDS::DBSnapshot'|'AWS::RDS::DBCluster'|'AWS::RDS::DBClusterSnapshot'|'AWS::RDS::EventSubscription'|'AWS::S3::Bucket'|'AWS::S3::AccountPublicAccessBlock'|'AWS::Redshift::Cluster'|'AWS::Redshift::ClusterSnapshot'|'AWS::Redshift::ClusterParameterGroup'|'AWS::Redshift::ClusterSecurityGroup'|'AWS::Redshift::ClusterSubnetGroup'|'AWS::Redshift::EventSubscription'|'AWS::SSM::ManagedInstanceInventory'|'AWS::CloudWatch::Alarm'|'AWS::CloudFormation::Stack'|'AWS::ElasticLoadBalancing::LoadBalancer'|'AWS::AutoScaling::AutoScalingGroup'|'AWS::AutoScaling::LaunchConfiguration'|'AWS::AutoScaling::ScalingPolicy'|'AWS::AutoScaling::ScheduledAction'|'AWS::DynamoDB::Table'|'AWS::CodeBuild::Project'|'AWS::WAF::RateBasedRule'|'AWS::WAF::Rule'|'AWS::WAF::RuleGroup'|'AWS::WAF::WebACL'|'AWS::WAFRegional::RateBasedRule'|'AWS::WAFRegional::Rule'|'AWS::WAFRegional::RuleGroup'|'AWS::WAFRegional::WebACL'|'AWS::CloudFront::Distribution'|'AWS::CloudFront::StreamingDistribution'|'AWS::Lambda::Function'|'AWS::NetworkFirewall::Firewall'|'AWS::NetworkFirewall::FirewallPolicy'|'AWS::NetworkFirewall::RuleGroup'|'AWS::ElasticBeanstalk::Application'|'AWS::ElasticBeanstalk::ApplicationVersion'|'AWS::ElasticBeanstalk::Environment'|'AWS::WAFv2::WebACL'|'AWS::WAFv2::RuleGroup'|'AWS::WAFv2::IPSet'|'AWS::WAFv2::RegexPatternSet'|'AWS::WAFv2::ManagedRuleSet'|'AWS::XRay::EncryptionConfig'|'AWS::SSM::AssociationCompliance'|'AWS::SSM::PatchCompliance'|'AWS::Shield::Protection'|'AWS::ShieldRegional::Protection'|'AWS::Config::ConformancePackCompliance'|'AWS::Config::ResourceCompliance'|'AWS::ApiGateway::Stage'|'AWS::ApiGateway::RestApi'|'AWS::ApiGatewayV2::Stage'|'AWS::ApiGatewayV2::Api'|'AWS::CodePipeline::Pipeline'|'AWS::ServiceCatalog::CloudFormationProvisionedProduct'|'AWS::ServiceCatalog::CloudFormationProduct'|'AWS::ServiceCatalog::Portfolio'|'AWS::SQS::Queue'|'AWS::KMS::Key'|'AWS::QLDB::Ledger'|'AWS::SecretsManager::Secret'|'AWS::SNS::Topic'|'AWS::SSM::FileData'|'AWS::Backup::BackupPlan'|'AWS::Backup::BackupSelection'|'AWS::Backup::BackupVault'|'AWS::Backup::RecoveryPoint'|'AWS::ECR::Repository'|'AWS::ECS::Cluster'|'AWS::ECS::Service'|'AWS::ECS::TaskDefinition'|'AWS::EFS::AccessPoint'|'AWS::EFS::FileSystem'|'AWS::EKS::Cluster'|'AWS::OpenSearch::Domain',
            #'AccountId': '633890674149'
        #     # 'Region': 'string'
        },
        GroupByKey= 'AWS_REGION',
        #Limit=123,
        #NextToken='string'
    )

    print(response)