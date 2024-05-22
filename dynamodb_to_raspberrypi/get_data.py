import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("utf-8")))

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883, 60)  # Connect to MQTT broker
client.subscribe("sensor/data")  # Subscribe to MQTT topic

client.loop_forever()  # Continue the network loop to receive messages
