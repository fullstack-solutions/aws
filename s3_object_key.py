import access_s3_bucket

def get_keys():
  resp = aws_utils.s3_data(bucket_name)
  for s3_obj in resp['Contents']:
    key = s3_obj['Key']
    return key
