

import boto3

s3 = boto3.client('s3')

s3.upload_file('index.html', 'aws-demo-github-kp', 'index.html')
