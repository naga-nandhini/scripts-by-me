import boto3

aws_con = boto3.session.Session(profile_name="sandbox")

ec2_dashboard = aws_con.resource(service_name ='ec2')

with open('instance-sand.txt' , 'w') as file:
  for instance in ec2_dashboard.instances.all():
    file.write(str(instance))
    file.write(str(instance.state))
    file.write('\n')
