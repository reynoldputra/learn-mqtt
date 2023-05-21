import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_publish(client, userdata, mid):
    print("Message published successfully")

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish

# Replace the following with your RabbitMQ MQTT broker details
broker_address = "localhost"
broker_port = 1883
username = "mqtt_user2"
password = "mqtt_password2"
# client.username_pw_set(username, password)

client.connect(broker_address, broker_port, 60)
result = client.publish("mytopic", "Hello, MQTT!")
if result.rc == mqtt.MQTT_ERR_SUCCESS:
    print("Message sent successfully")
else:
    print("Failed to send message")

client.disconnect()

