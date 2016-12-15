## Apache Kafka Demo
A simple Python producer and Javascript Consumer based on the Apache Kafka publish subscribe messaging application.

### Dependencies
Run the commands `npm install` and `pip install -r requirements.txt` to install the project dependencies.
You also need to have started the [Kafka](https://kafka.apache.org/quickstart) application and created a topic `kafka-python-topic`.

### Run
Run the command `node consumer/consumer.js` to start the consumer and `python producer/producer.py` to start the producer.
You should see the produced messages in the consumer's feed.
