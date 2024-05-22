# AWS DynamoDB to Raspberry Pi via MQTT

This project demonstrates how to send data from AWS DynamoDB to a Raspberry Pi using MQTT. The data stored in DynamoDB is transmitted to the Raspberry Pi, which subscribes to an MQTT topic to receive the data.


## Prerequisites

Before you begin, ensure you have the following:

- AWS account
- Raspberry Pi with Raspbian OS installed
- Python 3.x installed on Raspberry Pi
- AWS CLI configured on your local machine

## Setup AWS IoT

1. **Create an IoT Thing**:
    - Go to the AWS IoT Core console.
    - Create a new IoT thing.
    - Download the device certificate, private key, and root CA certificate.

2. **Attach a Policy to the Certificate**:
    - Create a policy with permissions to publish and subscribe to your MQTT topics.
    - Attach the policy to your device certificate.

3. **Create an IoT Rule**:
    - Create a rule to trigger data forwarding from DynamoDB to the MQTT topic.

## Setup DynamoDB

1. **Create a DynamoDB Table**:
    - Go to the DynamoDB console.
    - Create a new table with a primary key (`DEVID`) and sort key (`TIMES`).

2. **Insert Sample Data**:
    - Add some sample data to the DynamoDB table that will be sent to the Raspberry Pi.

## Raspberry Pi Setup

1. **Install AWS IoT SDK**:
    pip install AWSIoTPythonSDK
    

## Setup AWS IoT

1. **Create an IoT Thing**:
    - Go to the AWS IoT Core console.
    - Create a new IoT thing.
    - Download the device certificate, private key, and root CA certificate.

2. **Attach a Policy to the Certificate**:
    - Create a policy with permissions to publish and subscribe to your MQTT topics.
    - Attach the policy to your device certificate.

3. **Create an IoT Rule**:
    - Create a rule to trigger data forwarding from DynamoDB to the MQTT topic.

3. **Setup the MQTT Client**:
    - Create a Python script (`mqtt_publish.py`) on your Raspberry Pi to connect to the AWS IoT Core and subscribe to the MQTT topic.


## Running the Project
1. **connect to DynamoDB**:
Create a Python script (`dynamodb_query.py`) on your Raspberry Pi to connect to the with DynamoDB and retrieve data from table and store in a json file.


2. **Run the dynamodb_query and mqtt_publish on Raspberry Pi**:
    python dynamodb_query.py
    python mqtt_publish.py
    

3. **Send Data from DynamoDB to MQTT**:
    - Ensure your IoT rule is correctly set up to forward data from DynamoDB to the MQTT topic.


