import paho.mqtt.client as mqtt
from random import uniform
from pykafka import KafkaClient
import time

mqtt_broker = "mqtt.eclipseprojects.io"
mqtt_client = mqtt.Client("Temperature_Inside")
mqtt_client.connect(mqtt_broker)

kafka_client = KafkaClient(hosts="localhost:29092")
kafka_topic = kafka_client.topics['temperature']
kafka_producer = kafka_topic.get_sync_producer()

while True:
    randNumber = uniform(20.0, 21.0)
    mqtt_client.publish("temperature", randNumber)
    print("MQTT: Just published " + str(randNumber) + " to topic temperature")
    kafka_producer.produce(str(randNumber).encode('ascii'))
    print("KAFKA: Just published " + str(randNumber) + " to topic temperature")
    time.sleep(3)
