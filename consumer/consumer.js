const Kafka = require('no-kafka');

const consumer = new Kafka.SimpleConsumer
// data handler function can return a Promise
var dataHandler = function (messageSet, topic, partition) {
    messageSet.forEach(function (m) {
      // console.log(m.message.value);
        console.log(topic, partition, m.offset, m.message.value.toString('utf8'));
    });
};

return consumer.init().then(function () {
    // Subscribe partitons 0 and 1 in a topic:
    return consumer.subscribe('kafka-python-topic', [0] , dataHandler);
});
