from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

# AWS IoT Core endpoint
endpoint = "a2ehfo5qzc4dwp-ats.iot.ap-south-1.amazonaws.com"

# Paths to your certificate, private key, and root CA
root_ca_path = "certificates/AmazonRootCA1.pem"
certificate_path = "certificates/5617b3ce5b1d5f313c05ec4efe53736d50ccfca3a974b05707bd1c0bca9534cd-certificate.pem.crt"
private_key_path = "certificates/5617b3ce5b1d5f313c05ec4efe53736d50ccfca3a974b05707bd1c0bca9534cd-private.pem.key"


# Topic to publish data
topic = "my/topic"

# Read data from text file
with open("received_data.txt", "r") as file:
    data = file.read()

# Convert data to JSON
try:
    json_data = json.loads(data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
    exit(1)

# Convert JSON object back to string to prepare for MQTT publish
payload = json.dumps(json_data)

# Configure MQTT client
client = AWSIoTMQTTClient("raspberry_pi")
client.configureEndpoint(endpoint, 8883)
client.configureCredentials(root_ca_path, private_key_path, certificate_path)

# Connect to AWS IoT Core
client.connect()

# Publish data
client.publish(topic, payload, 1)
print("Data published to AWS IoT Core")

# Disconnect from AWS IoT Core
client.disconnect()
print("Disconnected from AWS IoT Core")
