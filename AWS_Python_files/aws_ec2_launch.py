#Adrian Guillory (Dack Dissident)
#06-02-2023

#Python program for launching an EC2 instance

#Enter in for Windows > Visual Studio > Terminal
#Type 'python -m pip install boto3' in terminal, then hit ENTER to install
#Restart Visual Studio

import boto3
from time import sleep

#Copy + paste AWS_Key from AWS
AWS_KEY="<AWS KEY HERE>"
#Copy + paste AWS Secret Access Key from AWS
AWS_SECRET="<AWS_SECRET HERE>"
#Copy + paste AWS Region
REGION="<REGION HERE>"
#Copy + paste AMI ID from AWS
AMI_ID = "<AMI_ID HERE>"
#Create Keypair 'cloud' in AWS > EC2 > Key Pairs 
# Copy + paste Key pair from AWS named 'cloud'
EC2_KEY_HANDLE = "cloud"
INSTANCE_TYPE="t2.nano"
#Get the default security group ID from AWS > EC2 > Security Groups
#Copy + paste secruity group ID
SECGROUP_ID="<SECGROUP_ID HERE>"

print("Connecting to EC2")

ec2 = boto3.client('ec2', aws_access_key_id=AWS_KEY, aws_secret_access_key=AWS_SECRET, region_name=REGION)

print ("Launching instance with AMI-ID %s, with keypair %s, \
       instance type %s, security group \
       %s"%(AMI_ID, EC2_KEY_HANDLE, INSTANCE_TYPE, SECGROUP_ID))

response = ec2.run_instances(ImageId=AMI_ID, KeyName=EC2_KEY_HANDLE, InstanceType=INSTANCE_TYPE, SecurityGroupIds = [ SECGROUP_ID, ], MinCount=1, MaxCount=1)

print (response)
Instance_ID=response['Instances'][0]['InstanceId']

print("Waiting for instance to be up and running")

response = ec2.describe_instances(InstanceIds=[Instance_ID])
status=response['Reservations'][0]['Instances'][0]['State']['Name']
print("Status" +str(status))

while status =='pending':
    sleep(10)
    response = ec2.describe_instances(InstanceIds=[Instance_ID])
    status=response['Reservations'][0]['Instances'][0]['State']['Name']
    print("Status: "+str(status))

if status =='running':
    response = ec2.describe_instances(InstanceIds=[Instance_ID])
    print("\nInstance is now running. Instance details are:")
    print("\nInstance Type: " + \
     str(response['Reservations'][0]['Instances'][0]['InstanceType']))
    print("Instance State: " + \
     str(response['Reservations'][0]['Instances'][0]['State']['Name']))
    print("Instace Launch Time: " + \
     str(response['Reservations'][0]['Instances'][0]['LaunchTime']))
    print("Instance Public DNS: " + \
     str(response['Reservations'][0]['Instances'][0]['PublicDnsName']))
    print("Instance Privatie DNS: " + \
     str(response['Reservations'][0]['Instances'][0]['PrivateDnsName']))
    print("Instance IP: " + \
     str(response['Reservations'][0]['Instances'][0]['PublicIpAddress']))
    print("Instance Private IP: " + \
     str(response['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
