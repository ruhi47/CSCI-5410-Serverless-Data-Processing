import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(region):
    # Create bucket
    try:
        s3_client = boto3.client('s3', region_name=region,
                                 aws_access_key_id='ASIARLJZH5IELHDFK6EZ',
                                 aws_secret_access_key='QV7FNdQQSGIKAHdm0ZffClYlqga3uH192KwnmKIQ',
                                 aws_session_token='FwoGZXIvYXdzEKj//////////wEaDB1wWtmobHo1khiHTSLAATI7isiA4GMCAqLhGJotSza84p+HRcJCkRGx+4eC494bESuyOSBSYBSoZlpJbPKyNOBu/2asVw0DrX8NyH5EgtpwJGrm5tEZH8E7K7Hqhfsp66hYGRetlVb8VY0DD1T8wjCAOhkibvA8QeS8rhFRwKfHa5rR5XLxPlt0kPhh9rHxGc2/8gf3+0C/r6IMzNjT6iZzkh4QMNF05S8I1UljtptHYInX1JfdvrgAeAMjItiraOoCGurNXYAGTeGROy/JayiSpt6VBjIt6+Sdr+ULFxowL67QkWM6uiKnu80UZlCp28ScZf1p+whiugJHFkaMQ68y9AWL'
                                 )
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket='source1b00872269',
                                CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
