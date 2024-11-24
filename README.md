# Real-Time Streaming Data Pipeline

## Project Overview
This project demonstrates a real-time data pipeline using Kafka and Spark. It ingests, processes, and stores streaming data into a Kafka topic.

### Features
- Ingest streaming data using a Kafka consumer.
- Transform, aggregate, or filter data using Spark.
- Store processed data in a new Kafka topic.

## Prerequisites
- Docker
- Python 3.8+
- Java 17
- PYSPARK_PYTHON,PYSPARK_DRIVER_PYTHON variables are set to python.exe path

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/satishavirneni/streaming-pipeline.git
   cd streaming-pipeline
   ```

2. Start the Docker containers:
   ```bash
   docker-compose up
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Kafka consumer:
   ```bash
   python pipeline.py
   ```
## Steps to verify contents in topics
1. Check Running containers
   ```bash
   docker-compose ps
   ```
   You should see services like kafka and zookeeper listed as Up

2. Access Kafka container
   ```bash
   docker exec -it real_time_streaming_pipeline-kafka-1 /bin/bash
   ```

3. List Available Kafka Topics
   ```bash
   kafka-topics --bootstrap-server localhost:9092 --list
   ```
   
4. View Kafka Topic Contents
   kafka-console-consumer --bootstrap-server localhost:9092 --topic <topic_name> --from-beginning
   Replace <topic_name> with the name of the topic (e.g., user-login or processed-user-login)
   ```bash
   kafka-console-consumer --bootstrap-server localhost:9092 --topic processed-user-login --from-beginning
   ```
