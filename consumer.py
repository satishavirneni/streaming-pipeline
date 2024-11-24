import logging
from kafka import KafkaConsumer
import json

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("KafkaConsumer")


def consume_messages(topic, bootstrap_servers='localhost:29092'):
    """
    Consumes messages from the given Kafka topic.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    )
    logger.info(f"Subscribed to topic: {topic}")

    for message in consumer:
        logger.info(f"Received message: {message.value}")
        yield message.value
