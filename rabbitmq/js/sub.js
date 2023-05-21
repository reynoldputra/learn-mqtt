const mqtt = require('mqtt');

// MQTT broker details
const brokerUrl = 'mqtt://localhost:1883';
const topic = 'mytopic';

// Create an MQTT client
const client = mqtt.connect(brokerUrl);

// Connect to the broker
client.on('connect', () => {
  console.log('Connected to MQTT broker');

  // Subscribe to the topic
  client.subscribe(topic, (err) => {
    if (err) {
      console.error('Failed to subscribe:', err);
    } else {
      console.log('Subscribed to topic:', topic);
    }
  });
});

// Handle received messages
client.on('message', (topic, message) => {
  console.log('Received message:', message.toString());

  // Disconnect from the broker after receiving a message (optional)
  client.end();
});

