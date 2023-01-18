import logging
import boto3
from botocore.exceptions import ClientError


def upload_file(bucket):
    # Upload the file
    s3_client = boto3.client('s3', region_name='us-east-1',
                             aws_access_key_id='ASIARLJZH5IEEO7WKHK5',
                             aws_secret_access_key='EXxOXA2v5IYzQa40ZbHlRJCoUOhj6aPrDCwVS6k4',
                             aws_session_token='FwoGZXIvYXdzEMn//////////wEaDOQmyY9KmAiUH+OsbCLAAYZFUqOo8OdZAymm9rrD6C3fFfe9nOxDuqqoyUL6aWMbyGVluRz0pMWr3SOMF2JjhxqCqcwe7sIqb/LUWapYSjrucy+ar0zvGS0dG80e6z4Fa7qmZvUTskAWN2PZLDFnej/dGH/mYLsThCCPSBFPSB5sQdYne76UI+l0j10K5iXQcmyb+eSLjlR72s3fxdstJbf0Oz+9OG8zf9SsTGB5dcnw20B4zU+ByMtuPlP5a55R8PdPsEK7ggEMtgpvkZbsCiic2p2WBjItWBMMt5YXD2cA+URIZ5Mv9mcfuNOC4zQlvKPQ2dVK15zK6mTMO3CtiG6boXkC'
                             )

    try:
        s3_client.upload_file('/Users/ruhityagi/Documents/Assignments_5410_SDP/Coding/assignment-4/file_mongo_tweets.txt', bucket, 'file_mongo_tweets.txt')
        print('File is pushed to {}'.format(bucket))
    except ClientError as e:
        logging.error(e)
        return False
    return True
