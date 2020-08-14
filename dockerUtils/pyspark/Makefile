spark-build:
	docker build -t pyspark .

spark-runtime:
	docker run -it --rm -v ${CURDIR}/data:/data -p 4040:4040 pyspark
