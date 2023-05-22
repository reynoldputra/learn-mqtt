from confluent_kafka import Consumer

# Kafka broker details
bootstrap_servers = 'localhost:29092'
topic = 'mytopic'
group_id = '123123'

# Create a Kafka consumer instance
consumer = Consumer({
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'  # Start consuming from the beginning of the topic
})

# Subscribe to the topic
consumer.subscribe([topic])

# Start consuming messages
try:
    while True:
        # Poll for new messages
        message = consumer.poll(timeout=1.0)

        if message is None:
            continue
        elif message.error() is not None:
            print(f"Error encountered: {message.error()}")
        else:
            # Process the received message
            print(f"Received message: {message.value().decode('utf-8')}")

except KeyboardInterrupt:
    # Stop consuming when interrupted
    pass

# Close the consumer
consumer.close()

