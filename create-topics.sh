#!/bin/bash

# Wait for Kafka to start
sleep 5

# Create the processed-user-login topic
 /usr/bin/kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --replication-factor 1 \
  --partitions 1 \
  --topic processed-user-login
