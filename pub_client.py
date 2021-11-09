import paho.mqtt.client as mqtt

HOST = "test.mosquitto.org"

def on_connect(client, userdata, flags, rc):
    print("Connected to host {HOST} with code ", str(rc))

# Create a client
client = mqtt.Client("nh_pub_client")
client.on_connect = on_connect

# Connect to the mqtt broker
client.connect(HOST)

# Publish a message
topic = "nhtest/peoplecount"
while True:
    print("Enter value to publish on topic {topic} (q to quit): ", end="")
    value = input()
    if value == "q":
        break
    client.publish(topic, value)

# Disconnect from client once finished
client.disconnect()

