FROM ubuntu:18.04

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
RUN ln -s /usr/bin/pip3 /usr/bin/pip

# Install PySpark and Numpy
RUN \
    pip install --upgrade pip && \
    pip install jupyterlab && \
    pip install numpy && \
    pip install pyspark && \
    pip install pyspark-stubs && \
    pip install pylint && \
    pip install ipykernel && \
    pip install autopep8 && \
    pip install kafka-utils && \
    pip install kafka-python && \
    pip install jupyter-tabnine && \
    jupyter nbextension install --py jupyter_tabnine && \
    jupyter nbextension enable --py jupyter_tabnine && \
    jupyter serverextension enable --py jupyter_tabnine

RUN ln -s /usr/bin/python3 /usr/bin/python

# Define working directory
WORKDIR /data

# Define default command
CMD ["bash"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
