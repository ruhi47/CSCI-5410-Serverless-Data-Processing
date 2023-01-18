import json
import urllib.parse
import boto3
from datetime import datetime

print('Loading function')

s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        var1 = response["Body"].read().decode('utf-8')
        json_data = json.loads(var1)
        key1 = key.split(":")[0]
        print(key1, json_data.items())
        for k, v in json_data.items():
            dynamodb.put_item(TableName='assignment3', Item={'NamedEntity': {'S': k}, 'Frequency': {'N': str(v)},
                                                             'TimeStamp': {'S': str(datetime.now())}})
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print(
            'Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(
                key, bucket))
        raise e
