from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time

# AWS IoT Core endpoint
endpoint = "a2ehfo5qzc4dwp-ats.iot.ap-south-1.amazonaws.com"


# Paths to your certificate, private key, and root CA
root_ca_path = "aws_certificates/root.pem"
certificate_path = "aws_certificates/certificate.pem.crt"
private_key_path = "aws_certificates/private.pem.key"

# Topic to publish data
topic = "sensor/data"

# Read data from text file
with open("mqtt_message.json", "r") as file:
    data = file.read()

# Function to publish data
def publish_data(client, userdata, message):
    print("Data published to AWS IoT Core")

# Configure MQTT client
client = AWSIoTMQTTClient("raspberry_pi")
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(root_ca_path, private_key_path, certificate_path)

# Connect to AWS IoT Core
client.connect()

# Publish data
client.publish(topic, data, 1)

# Disconnect from AWS IoT Core
client.disconnect()

