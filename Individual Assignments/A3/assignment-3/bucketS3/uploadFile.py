import logging
import os
import time
import boto3
from botocore.exceptions import ClientError


def upload_file(bucket):
    # Upload the file

    s3_client = boto3.client('s3', region_name='us-east-1',
                             aws_access_key_id='ASIARLJZH5IEBFN6UDQM',
                             aws_secret_access_key='lF4TLRqXtS7AM2qnWDczs6NNtJsPASObujwhemIr',
                             aws_session_token='FwoGZXIvYXdzEMX//////////wEaDP5olk7jqIkXadFANiLAAaCX3OA9UXyzplsG8RlZxB3HL/e8i1sRT+w/VXaRoGAGYYYUcsld5pdiG2hFFcPXgILXPC4LzyKf2XBlRE5MnRW6v99Q2/YrVIEhGYHRK8T7eyeE6J+X9d1XgczE4+lxNW/oMewY1MoOb7a4/kUrn6jmJuQeqf1LvYABbu9QX7BNhwMIY6GwebqS72os5kXTxFGVP0Vkw1wc374GlSLfmgPyBMGOlJK7mPMx+uHdRldJ6JkB4x3gMUbGhRtuwmTfpSivweSVBjIt+eYixlruRgbsUI48cT8E7Fw+YopyP1t7WmCCoH037WtcRYKHDlzVn/D++C55'
                             )

    try:
        for i in range(1, 7):
            s3_client.upload_file('/Users/ruhityagi/PycharmProjects/bucketS3/tech/00' + str(i) + '.txt', bucket,
                                  '00' + str(i) + '.txt')
            print('00' + str(i) + '.txt is being pushed to {}'.format(bucket))
            # Adding delay of 200ms to upload file
            print('Delay of 200ms added!')
            time.sleep(0.2)

    except ClientError as e:
        logging.error(e)
        return False
    return True
