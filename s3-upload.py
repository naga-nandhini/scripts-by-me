import boto3 
aws_console=boto3.session.Session(profile_name="nandy")
client=aws_console.client("s3")
bucket_name=input("Enter the bucket name: ")
file_name=input("Enter the file name:")
response = s3.client.upload_file(bucket_name=bucket_name,file_name=file_name)
print("Uploaded Sucessfuly")
