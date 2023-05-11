import boto3 

aws_console = boto3.session.Session(profile_name='nandhini-nallamuthu')
autoscaling = aws_console.client('autoscaling')

autoscaling_name = input("Enter the AutoScalingGroupName : ")

min_size = input("Enter the min size : ")
try:
    min_size = int(min_size)
except ValueError:
    print("Invalid input for max size. Please enter a valid integer.")
    exit(1)

max_size = input("Enter the max size: ")
try:
    max_size = int(max_size)
except ValueError:
    print("Invalid input for max size. Please enter a valid integer.")
    exit(1)

desired_capacity = input("Enter the desired_capacity: ")
try:
   desired_capacity = int(desired_capacity)
except ValueError:
    print("Invalid input for max size. Please enter a valid integer.")
    exit(1)

response = autoscaling.update_auto_scaling_group(
	AutoScalingGroupName=autoscaling_name,
	MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity
	)

print(f"The {autoscaling_name} is updated with {min_size} , {max_size} , {desired_capacity}")
