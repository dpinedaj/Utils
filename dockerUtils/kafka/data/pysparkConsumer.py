#Imports and running findspark

import pyspark
from pyspark import RDD
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json
#Spark context details
sc = SparkContext(appName="PythonSparkStreamingKafka")
ssc = StreamingContext(sc,2)
#Creating Kafka direct stream
dks = KafkaUtils.createDirectStream(ssc, ["testDB.dbo.fruit"], {"metadata.broker.list":"kafka:9092"})
counts = dks.pprint()
#Starting Spark context
ssc.start()
ssc.awaitTermination()