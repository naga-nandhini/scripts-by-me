import boto3

aws_console = boto3.session.Session(profile_name="nandhini-nallamuthu")
client = aws_console.client('s3')

user_action = input("Do you want to (create/upload)")

if user_action.lower() == "create" :
    bucket_name = input("Enter the bucket name: ")
    try:
        response = client.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-1'})
        print(f"The {bucket_name} bucket is successfully created")
    except Exception as e:
            print("Error uploading file:", str(e))

elif user_action.lower() == "upload":
    bucket_name = input("Enter the bucket name: ")
    file_path = input("Enter the path which you have file in your local : ") 
    object_name = input("Enter the file : ")
    try:
        response = client.upload_file(file_path, bucket_name, object_name)
        print("Your file was uploaded successfully.")
    except Exception as e:
        print("Error uploading file:", str(e))

else: 
    print("No actions is happened")
