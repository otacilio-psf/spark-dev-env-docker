FROM datamechanics/spark:3.1.1-hadoop-3.2.0-java-11-scala-2.12-python-3.8-dm14

USER root:root

ENV PYSPARK_MAJOR_PYTHON_VERSION=3

RUN pip3 install --upgrade pip

RUN pip3 install jupyterlab==3.1.14 pyspark==3.1.1

COPY ./jars/ /opt/spark/jars

EXPOSE 8888
