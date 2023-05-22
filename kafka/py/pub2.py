from confluent_kafka import Producer

# Kafka broker details
bootstrap_servers = 'localhost:29092'
topic = 'mytopic'

# Create a Kafka producer instance
producer = Producer({
    'bootstrap.servers': bootstrap_servers
})

# Produce a message
message = 'Hello, Kafka!'
producer.produce(topic, value=message.encode('utf-8'))

# Flush the producer to ensure the message is sent
producer.flush()

# Close the producer
# producer.close()

