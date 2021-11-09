import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    """ The callback for when the client receives a CONNACK response from the server"""
    print("Connected with code ", str(rc))
    topic = "nhtest/peoplecount"
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Recevied message on topic {msg.topic}:, {str(msg.payload)}")

# Create client
client = mqtt.Client("nh_sub_client")
client.on_connect = on_connect
client.on_message = on_message

# Connect to mqtt broker
client.connect("test.mosquitto.org")
# on_connect() callback will run upon successful connection
# on_message() callback will run whenever a message is published

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
