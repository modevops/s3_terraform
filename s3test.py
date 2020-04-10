import boto3


bucket_name = 'aetna-s3'
s3_client = boto3.client('s3')

versions = s3_client.list_object_versions(Bucket=bucket_name)

for version in versions:
    version_id = versions['Versions'][0]['VersionId']
    file_key = versions['Versions'][0]['Key']

    response = s3.get_object(
        Bucket=bucket_name,
        Key=file_key,
        VersionId=version_id,
    )
    data = response['Body'].read()
    print(data)