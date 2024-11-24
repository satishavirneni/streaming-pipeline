import unittest
from unittest.mock import patch, MagicMock
from pyspark.sql import SparkSession
from pipeline import main
from processor import process_data


class TestPipelineWithSpark(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Initialize a Spark session for the test suite.
        """
        cls.spark = SparkSession.builder \
            .appName("TestPipeline") \
            .master("local[*]") \
            .config("spark.driver.allowMultipleContexts", "true") \
            .config("spark.ui.enabled", "false") \
            .getOrCreate()

    @classmethod
    def tearDownClass(cls):
        """
        Stop the Spark session after tests.
        """
        cls.spark.stop()

    @patch('pipeline.consume_messages')
    @patch('pipeline.produce_message')
    def test_pipeline_execution_with_spark(self, mock_produce_message, mock_consume_messages):
        """
        Test the full pipeline workflow with Spark integration.
        """
        # Mock Kafka consumer to yield sample messages
        raw_messages = [
            {"user_id": "123", "app_version": "2.3.0", "device_type": "android", "locale": "US",
             "timestamp": "1694479551"},
            {"user_id": "456", "app_version": "2.4.0", "device_type": "ios", "locale": "IN", "timestamp": "1694479552"},
            {"user_id": "789", "app_version": "1.0.0", "device_type": "desktop", "locale": "FR",
             "timestamp": "1694479553"},  # Invalid
        ]
        mock_consume_messages.return_value = raw_messages

        # Mock producer to track calls
        mock_produce_message.return_value = None

        # Run the pipeline
        main(2)

        # Verify consumer was called
        mock_consume_messages.assert_called_once_with('user-login')

        # Verify producer was called with processed messages
        # Process the raw messages using the real Spark-based process_data
        processed_messages = process_data(raw_messages)
        # Ensure producer was called for each valid processed message
        for message in processed_messages:

            mock_produce_message.assert_any_call('processed-user-login', message)

        # Verify the number of processed messages matches the expected output
        self.assertEqual(mock_produce_message.call_count, len(processed_messages))
        self.assertGreater(len(processed_messages), 0)  # Ensure some messages were processed


if __name__ == "__main__":
    unittest.main()
