import boto3

aws_console = boto3.session.Session(profile_name='prod')

client = aws_console.client('s3')

response = client.list_buckets()

with open("s3-prod-bucket-name.txt",'w') as file:
 for bucket in response['Buckets']:
  name = str(bucket['Name'])
  date = str(bucket['CreationDate'])
  file.write(name)
  file.write(date)
  file.write('\n')
