import boto3

# which service or services you’re going to use:
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# client = boto3.client('ssm',region_name='ap-south-1')

# response = client.get_parameter(
#     Name='param-custom',
#     WithDecryption=True
# )

# print(response['parameter']['value'])