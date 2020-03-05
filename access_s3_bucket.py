import boto3


##for accessing the bucket using cross role change the session by session = boto3.Session(profile_name=Profile name in config)

s3 = boto3.client("s3")

# s3 object content
def get_data_body(key, bucket_name):
    s3_object = s3.get_object(Bucket=bucket_name, Key=key)
    
    ##decode change the the data of file to string
    object_body = s3_object['Body'].read().decode()  
    
    ##Split the data in array if its is text file
    body = object_body.split('\n') 
    return body

# List of s3 bucket all files
def s3_data(bucket_name):
    resp = s3.list_objects_v2(Bucket=bucket_name)
    return resp
