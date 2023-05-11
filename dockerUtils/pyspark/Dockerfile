FROM python:3.9-buster

ARG spark_uid=185

RUN apt update && \
    apt install -y openjdk-11-jre openjdk-11-jdk wget zip && \
    rm -rf /var/cache/apt/*

RUN wget https://dlcdn.apache.org/spark/spark-3.2.2/spark-3.2.2-bin-hadoop3.2.tgz \
    && tar -xvf spark-3.2.2-bin-hadoop3.2.tgz \
    && mv spark-3.2.2-bin-hadoop3.2 /opt/spark \
    && rm spark-3.2.2-bin-hadoop3.2.tgz

ENV SPARK_HOME="/opt/spark"
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
ENV PATH=${PATH}:${SPARK_HOME}/bin:${SPARK_HOME}/sbin:${JAVA_HOME}/bin:${SPARK_HOME}/python
RUN echo "SPARK_LOCAL_IP=127.0.0.1" > $SPARK_HOME/conf/spark-env.sh



# Specific
ARG CODE_PATH=/opt/code
RUN mkdir -p ${CODE_PATH}
ENV PYTHONPATH=${SPARK_HOME}/python:${SPARK_HOME}/python/lib/py4j-0.10.9.3-src.zip:${CODE_PATH}:${PYTHONPATH}

# COPY jars/* ${SPARK_HOME}/jars/
