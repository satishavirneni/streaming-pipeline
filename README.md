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
   ```## Steps to verify contents in topics
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

5. How would you deploy this application in production?
   Approach#1: We can Deploy the application directly to Databricks, Dataproc or AWS EMR by creating a wheel file through a CI/CD pipeline using tools like Jenkins. 
   Use variables for configurations like the Kafka bootstrap server and Kafka topic names to ensure flexibility. 
   Set up a Databricks, Dataproc or AWS EMR job cluster to run the pipeline 24/7, with email notifications configured for any job failures during execution. 
   The Spark logs can be reviewed for detailed debugging. Implement checkpointing for fault tolerance to recover from failures. 
   For data processing and storage, leverage Azure Storage Accounts, AWS S3, or Google Cloud Storage, depending on the cloud provider.
   
   Approach#2: We can deploy the application directly to Kubernetes by creating a Docker image and storing it in container services like Azure Container Registry (ACR), Amazon Elastic Container Registry (ECR), or Google Artifact Registry (AR). 
   A dedicated Kubernetes pipeline can be set up in a GitHub repository. This pipeline will include a Helm chart to manage deployment, with all variables such as the bootstrap server and Kafka topics passed as Helm parameters. 
   Deployment can be automated through CI/CD pipelines using tools like Jenkins. 
   To monitor the application, enable Grafana and Loki for metrics and centralized logging.
   
6. What other components would you want to add to make this production ready?
   Databricks: Deploy Spark jobs with checkpointing for fault tolerance, use job clusters for 24/7 execution, and enable alerting via email for failures.
   Dataproc/EMR: Run managed Spark clusters for processing, store checkpoints in cloud storage (GCS/S3), and use auto-scaling for cost optimization.
   Kubernetes: Containerize the application, deploy using Helm charts with variables for Kafka and storage, and set up CI/CD with Jenkins. Use Grafana and Loki for monitoring and centralized logging.
   
7. How can this application scale with a growing dataset?
   Cluster Auto scaling: Enable the auto scaling in Databricks, Emr or Dataproc to dynamically to adjust the resources based on work loads/Data movement.
   Optimize the spark jobs: Use partitioning and bucketing to reduce the shuffle operation between the executors.
   Checkpointing: Store spark checkpoints in storage like AWS s3, GCS or Azure storage accounts to ensure recovery and avoid recomputation. 