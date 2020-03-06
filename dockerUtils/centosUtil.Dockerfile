FROM centos:7
#Actualizar e instalar todos los paquetes necesarios
RUN yum update -y \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip \
    && yum install -y which gcc \ 
    && yum install -y openldap-devel \
    && yum install -y wget \
    && yum install -y libaio

# Crear el link simbolico de python y pip
RUN ln -s /usr/bin/pip3.6 /bin/pip
# Instalar paquetes de python
RUN pip install --upgrade pip
