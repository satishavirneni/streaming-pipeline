import logging
from kafka import KafkaProducer
import json

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("KafkaProducer")


def produce_message(topic, message, bootstrap_servers='localhost:29092'):
    """
    Produces a message to the given Kafka topic.
    """
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
    )
    producer.send(topic, value=message)
    producer.flush()
    logger.info(f"Published message to topic: {topic} | Message: {message}")
