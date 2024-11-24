# Design Decisions

## Data Flow
1. **Data Generation**:
   - The data generator produces login events in the `user-login` Kafka topic.

2. **Kafka Consumer**:
   - Consumes events, processes them, and adds derived fields.

3. **Data Transformation**:
   - Spark is used for scalable and efficient data processing.

4. **Kafka Producer**:
   - Stores transformed data in the `processed-user-login` Kafka topic.

## Production-Readiness Enhancements
1. **Monitoring**:
   - Use Prometheus and Grafana for pipeline monitoring.
2. **Error Handling**:
   - Implement retries and dead-letter queues.
3. **Scalability**:
   - Deploy Spark on a distributed cluster.

## Deployment
- Use Kubernetes for container orchestration.
- Leverage CI/CD pipelines for continuous integration and deployment.
