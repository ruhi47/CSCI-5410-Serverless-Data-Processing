import json
import urllib.parse
import re

import boto3

print('Loading function')

s3_client = boto3.client('s3', region_name='us-east-1',
                         aws_access_key_id='ASIARLJZH5IEBTCUQXWB',
                         aws_secret_access_key='tjxOEK2AVtiUL1/e4RjMYBO91ovfkdPLf6ehV/2t',
                         aws_session_token='FwoGZXIvYXdzEOP//////////wEaDKohCECUKwMBDQq29iLAAX3REKh9fub1mxPgG9Gcu6/daO7jVgMBcR1Y6J7AqcA/enRbvnaR8LHL4iMfeJz/lY7ihs0JjrCIM34d1kgKeRGPp6E10J83mHCDwzxjiNIrQALNuH49h5b+jPQiJR+S2kAUwkx3aEppN/KdwkP1olA4Iyoq9MxFOmxCld8k1JXj4lfZ2vAzYXy4k1miwBCwcyAnBmXy93JW2zUvRlSXpdFmxzZsJPppVqYlaCZz1hPRB5B3nySbYrVBuwUwWyTtQyjAvKOWBjIthN18KPasyDrGIsSNV1oq2yjVBSzHwsm+4LrHjehiW4wcZfRK8f8JN2dsyk+A'
                         )

comprehend = boto3.client('comprehend', region_name='us-east-1',
                          aws_access_key_id='ASIARLJZH5IEBTCUQXWB',
                          aws_secret_access_key='tjxOEK2AVtiUL1/e4RjMYBO91ovfkdPLf6ehV/2t',
                          aws_session_token='FwoGZXIvYXdzEOP//////////wEaDKohCECUKwMBDQq29iLAAX3REKh9fub1mxPgG9Gcu6/daO7jVgMBcR1Y6J7AqcA/enRbvnaR8LHL4iMfeJz/lY7ihs0JjrCIM34d1kgKeRGPp6E10J83mHCDwzxjiNIrQALNuH49h5b+jPQiJR+S2kAUwkx3aEppN/KdwkP1olA4Iyoq9MxFOmxCld8k1JXj4lfZ2vAzYXy4k1miwBCwcyAnBmXy93JW2zUvRlSXpdFmxzZsJPppVqYlaCZz1hPRB5B3nySbYrVBuwUwWyTtQyjAvKOWBjIthN18KPasyDrGIsSNV1oq2yjVBSzHwsm+4LrHjehiW4wcZfRK8f8JN2dsyk+A'
                          )


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    try:
        bucket = 'twitterdatab00872269'
        key = 'file_mongo_tweets.txt'
        response = s3_client.get_object(Bucket=bucket, Key=key)
        paragraph = response["Body"].read().decode('utf-8')
        paragraph = paragraph.split('\n\n')
        print(len(paragraph))
        result = []
        for i in range(len(paragraph)):
            try:
                if len(paragraph[i]) and len(paragraph[i].encode('utf-8')) <= 5000:
                    sentiment = comprehend.detect_sentiment(Text=paragraph[i], LanguageCode="en")
                    sentiment["tweet"] = paragraph[i]
                    result.append(sentiment)
            except Exception as e:
                print(e)
        s3_client.put_object(Bucket='twitterdataoutputb00872269', Key='output.json', Body=json.dumps(result))

        return response['ContentType']
    except Exception as e:
        print(e)
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e
