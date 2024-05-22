import json
import boto3
from boto3.dynamodb.types import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RaspberryPiTable')  # Replace with your table name

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        # Parse the IoT message from the event
        for record in event['Records']:
            payload = record['body']
            data = json.loads(payload)
            
            # Write to DynamoDB
            table.put_item(Item=data)
            
        return {
            'statusCode': 200,
            'body': json.dumps('Data inserted successfully')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to insert data')
        }
