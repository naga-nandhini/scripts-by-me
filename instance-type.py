import boto3 
profile_name= input("Enter the env name (prod/sandbox) : ")
aws_console = boto3.session.Session(profile_name=profile_name)
ec2 = aws_console.client('ec2')

user =  input("Do you want to change instance type? (yes/no): ")

if user == "yes":
 instance_id = input("Enter the instance id: ")
 response = ec2.describe_instances(InstanceIds=[instance_id])
 state = response['Reservations'][0]['Instances'][0]['State']['Name']
 print(f"The current state of instance is {instance_id} is {state}.")

 if state == "running" or "stopped":
  ec2.stop_instances(InstanceIds=[instance_id])
  waiter = ec2.get_waiter('instance_stopped')
  waiter.wait(InstanceIds=[instance_id])
  print(f"The instance {instance_id} has been stopped.") 

  new_type = input("Enter the new instance type: ")
  response = ec2.modify_instance_attribute(
  InstanceId = instance_id,
  Attribute = 'instanceType',
  Value = new_type
)
 print(f"The instance type of this {instance_id} is {new_type}")
 ec2.start_instances(InstanceIds=[instance_id])
 waiter = ec2.get_waiter('instance_running')
 waiter.wait(InstanceIds=[instance_id])
 print(f"The instance {instance_id} has been running.")
