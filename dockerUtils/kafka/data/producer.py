from time import sleep
from json import dumps
from kafka import KafkaProducer
TOPIC = 'test-topic'


producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


for e in range(1000):
    print()
    data = {'number' : e}
    producer.send(TOPIC, value=data)
    sleep(5)