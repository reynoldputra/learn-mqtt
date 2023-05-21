const mqtt = require('mqtt');

// MQTT broker details
const brokerUrl = 'mqtt://localhost:1883';
const topic = 'mytopic';

// Create an MQTT client
const client = mqtt.connect(brokerUrl);

// Connect to the broker
client.on('connect', () => {
  console.log('Connected to MQTT broker');

  // Publish a message
  const message = 'Hello, MQTT!';
  client.publish(topic, message, (err) => {
    if (err) {
      console.error('Failed to publish message:', err);
    } else {
      console.log('Message published successfully');
    }

    // Disconnect from the broker
    client.end();
  });
});

