from kafka import KafkaProducer
import json

# from kafka import KafkaConsumer

# Let's make an instance of the Kafka Producer
# Keep in mind the requirements of the Producer Config object
# Broker-list, Key and value serialisers
# Kafka-python will provide the key and value serialisers as default string
# serialisers
# The producer record requires the fields: topic and message
#
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for message in range(5):
    producer.send('kafka-python-topic', {'values': message})

# consumer = KafkaConsumer('kafka-python-topic')
# for message in consumer:
#     print(message)
