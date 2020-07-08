FROM centos:7

#Variable del entorno
ENV ENTORNO ='DESARROLLO'
ENV LANG='es_ES.UTF-8'
RUN echo LANG="es_ESP.UTF-8" > /etc/locale.conf

#Generar variables de entorno necesarias

ENV C_FORCE_ROOT="true"

#Actualizar e instalar todos los paquetes necesarios
RUN yum update -y \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && yum install -y which gcc \ 
    && yum install -y openldap-devel \
    && yum install -y wget \
    && yum install -y libaio
# Instalar el driver para Oracle
RUN wget https://download.oracle.com/otn_software/linux/instantclient/195000/oracle-instantclient19.5-basic-19.5.0.0.0-1.x86_64.rpm
RUN rpm -i oracle-instantclient19.5-basic-19.5.0.0.0-1.x86_64.rpm
RUN rm oracle-instantclient19.5-basic-19.5.0.0.0-1.x86_64.rpm
# Crear el link simbolico pip
RUN ln -s /usr/bin/pip3.6 /bin/pip
# Instalar paquetes de python
RUN pip install psycopg2-binary alembic \
    boto3 s3fs cx-Oracle pyarrow pycryptodome configparser
# Crear los directorios necesarios
RUN mkdir
# Copiar los archivos necesarios
COPY 

