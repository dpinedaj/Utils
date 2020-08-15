FROM ubuntu:latest

# Install OpenJDK 11 --->Can use 8
RUN \
  apt-get update && \
  apt-get install -y openjdk-11-jdk && \
  rm -rf /var/lib/apt/lists/*

# Install Python
RUN \
    apt-get update && \
    apt-get install -y wget python3 python3-pip python3-dev virtualenv vim &&\
    rm -rf /var/lib/apt/lists/*

#Simbolic link for pip
RUN ln -s /bin/pip3 /bin/pip

# Install PySpark and Numpy
RUN \
    pip install --upgrade pip && \
    pip install numpy && \
    pip install pyspark && \
    pip install pyspark-stubs && \
    pip install pylint

#RUN rm /bin/python
RUN ln -s /bin/python3 /bin/python

# Define working directory
WORKDIR /data

# Define default command
CMD ["bash"]