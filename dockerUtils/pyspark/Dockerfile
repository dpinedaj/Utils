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
    #pip install "jedi==0.17" && \
    pip install "ipython==7.1.1" && \
    pip install "jupyterlab==3.0.16" && \
    pip install "numpy==1.19.5" && \
    pip install "pyspark==3.0.3" && \
    pip install "pyspark-stubs==3.0.0.post1" && \
    pip install "pylint==2.9.3" && \
    pip install "ipykernel==5.5.5" && \
    pip install "autopep8==1.5.7" && \
    pip install "kafka-utils==2.3.0" && \
    pip install "kafka-python==1.4.7" && \
    pip install "jupyter-tabnine==1.2.2" && \
    jupyter nbextension install --py jupyter_tabnine && \
    jupyter nbextension enable --py jupyter_tabnine && \
    jupyter serverextension enable --py jupyter_tabnine

RUN ln -s /usr/bin/python3 /usr/bin/python

# Define working directory
WORKDIR /data

# Define default command
CMD ["bash"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
