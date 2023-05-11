import boto3
profile_name=input("Enter the env name (prod/sandbox) : ")
region_name = input("Enter the AWS region name: ")
aws_console = boto3.Session(region_name=region_name,profile_name=profile_name)
ec2 = aws_console.client('ec2')
instance_id = input("Enter the instance ID: ")
response = ec2.describe_instances(InstanceIds=[instance_id])
state = response['Reservations'][0]['Instances'][0]['State']['Name']
print(f"The current state of instance is {instance_id} is {state}.")

if state == "running" or "stopped":
  ec2.stop_instances(InstanceIds=[instance_id])
  waiter = ec2.get_waiter('instance_stopped')
  waiter.wait(InstanceIds=[instance_id])
  print(f"The instance {instance_id} has been stopped.") 
  modify_attributes = True
      elif modify_attributes is True: 
          response = ec2.modify_instance_attribute(
          InstanceId=instance_id,
           DisableApiTermination={'Value': False})
           ec2.terminate_instances(InstanceIds=[instance_id])
           waiter = ec2.get_waiter('instance_terminated')
           waiter.wait(InstanceIds=[instance_id])
           print(f"Instance {instance_id} has been terminated.")

          else :
            print(f"Instance {instance_id} was already terminated.")
  
