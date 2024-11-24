from consumer import consume_messages
from processor import process_data
from producer import produce_message


def main(batch_size=50):
    source_topic = 'user-login'
    destination_topic = 'processed-user-login'

    batch_data = []

    for raw_message in consume_messages(source_topic):
        batch_data.append(raw_message)

        # Process the batch when it reaches the specified size
        if len(batch_data) >= batch_size:
            processed_messages = process_data(batch_data)

            # Publish processed messages
            for msg in processed_messages:
                produce_message(destination_topic, msg)

            # Clear batch
            batch_data = []
        # Process any remaining messages in the batch
    if batch_data:
        processed_messages = process_data(batch_data)
        for message in processed_messages:
            produce_message(destination_topic, message)


if __name__ == "__main__":
    main()
