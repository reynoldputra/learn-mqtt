import paho.mqtt.client as mqtt 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("mytopic")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Replace the following with your RabbitMQ MQTT broker details
broker_address = "localhost"
broker_port = 1883
username = "mqtt_user2"
password = "mqtt_password2"
# client.username_pw_set(username, password)

client.connect(broker_address, broker_port, 60)
client.loop_forever()
