from pyspark import SparkContext
sc = SparkContext("local[*]", "Test")

rdd = sc.parallelize(list(range(10)))

for i in rdd.collect():
    print(i)
