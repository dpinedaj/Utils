from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

TOPIC = 'test-topic'
consumer = KafkaConsumer(
    TOPIC,
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('mongodb:27017', username='admin', password='admin')
collection = client.test.test


for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
    #print(message)