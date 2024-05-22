import boto3
import json
from decimal import Decimal  # Import Decimal module

# Custom JSON encoder class to handle Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('RaspberryPiTable')

# Query DynamoDB table and retrieve data
response = table.scan()
data = response['Items']  # Assuming your data is stored as a list of dictionaries

# Convert data to MQTT message format (e.g., JSON)
mqtt_message = {"data": data}

# Save mqtt_message to a file or send it to MQTT publishing script
# For simplicity, let's assume you save it to a file
with open('mqtt_message.json', 'w') as f:
    json.dump(mqtt_message, f, cls=DecimalEncoder)  # Use the custom encoder class
