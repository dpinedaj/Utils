FROM almondsh/almond

# COPY *.ipynb ./
COPY ./jars/*.jar libs/
ADD https://repo1.maven.org/maven2/com/idealista/format-preserving-encryption/1.0.0/format-preserving-encryption-1.0.0.jar \
    https://repo1.maven.org/maven2/com/oracle/database/jdbc/ojdbc8/19.7.0.0/ojdbc8-19.7.0.0.jar \
    https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop2-latest.jar \
    https://storage.googleapis.com/spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
    https://repo1.maven.org/maven2/org/apache/spark/spark-avro_2.12/3.0.1/spark-avro_2.12-3.0.1.jar \
    libs/


USER jovyan
RUN \
    pip install --upgrade pip && \
    #pip install "jedi==0.17" && \
    pip install "ipython==7.18.1" && \
    pip install "jupyterlab==2.2.8" && \
    pip install "numpy==1.21.0" && \
    pip install "pyspark==3.0.3" && \
    pip install "pyspark-stubs==3.0.0.post1" && \
    pip install "pylint==2.9.3" && \
    pip install "ipykernel==5.3.4" && \
    pip install "autopep8==1.5.7" && \
    pip install "kafka-utils==2.3.0" && \
    pip install "kafka-python==1.4.7" && \
    pip install "jupyter-tabnine==1.2.2"

USER root
RUN chown -R jovyan: ./*
RUN mkdir /data
RUN chown -R jovyan: /data
RUN \
    jupyter nbextension install --py jupyter_tabnine && \
    jupyter nbextension enable --py jupyter_tabnine && \
    jupyter serverextension enable --py jupyter_tabnine
USER jovyan


# RUN for i in *.ipynb; do echo Running $i; jupyter nbconvert "$i" --execute --stdout --to asciidoc --ExecutePreprocessor.timeout=86400; done
WORKDIR /data