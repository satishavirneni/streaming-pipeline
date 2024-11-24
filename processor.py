from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, lit
import logging

# Configure logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SparkProcessor")

# Initialize Spark session (singleton pattern for reusability)
spark = SparkSession.builder \
    .config("spark.driver.bindAddress", "localhost") \
    .appName("KafkaStreamProcessor") \
    .getOrCreate()


def process_data(batch_data):
    """
    Processes a batch of incoming data using Spark for scalable transformations and aggregations.

    :param batch_data: List of dictionaries representing raw data.
    :return: List of dictionaries containing processed data.
    """
    logger.info(f"Processing batch of size: {len(batch_data)}")

    # Convert incoming data to Spark DataFrame
    df = spark.createDataFrame(batch_data)

    # Filtering: Remove invalid records (e.g., unsupported app versions, invalid locales)
    supported_app_versions = ["2.3.0", "2.4.0"]
    valid_locales = {"US", "IN", "RU", "UK"}

    filtered_df = df.filter(
        (col("app_version").isin(supported_app_versions)) &
        (col("locale").isin(valid_locales))
    )

    # Transformation: Add derived fields
    transformed_df = filtered_df.withColumn(
        "is_mobile", when(col("device_type").rlike("(?i)android|ios"), lit(True)).otherwise(lit(False))
    ).withColumn(
        "frequent_user", lit(False)  # Placeholder; can be updated based on historical data
    )

    # Aggregation: Count logins by locale and device type
    locale_counts = transformed_df.groupBy("locale").agg(count("*").alias("locale_login_count"))
    device_counts = transformed_df.groupBy("device_type").agg(count("*").alias("device_type_login_count"))

    # Join aggregation results back to the transformed data
    final_df = transformed_df \
        .join(locale_counts, on="locale", how="left") \
        .join(device_counts, on="device_type", how="left") \
        .withColumn(
        "high_login_locale", when(col("locale_login_count") > 100, lit(True)).otherwise(lit(False))
    )

    # Convert Spark DataFrame back to a list of dictionaries
    processed_data = [row.asDict() for row in final_df.collect()]

    logger.info(f"Processed batch data: {processed_data}")
    return processed_data
