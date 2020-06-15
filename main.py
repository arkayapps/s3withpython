import boto3
from config import config

s3 = boto3.client(
    's3',
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key']
)

# Upload
# s3.upload_file('/path/file', 'bucket_name', 'file_name_on_server')
s3.upload_file('hello.txt', config['bucket_name'], 'hello.txt')

# Download
# s3.download_file('bucket_name', 'file_name_on_server', '/path/file')
s3.download_file(config['bucket_name'], 'hello.txt', 'FILE_NAME')
