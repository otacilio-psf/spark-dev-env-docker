FROM otaciliopsf/spark-py:v3.1.1-hadoop3.2-abfss-delta

USER root:root

ENV PYSPARK_MAJOR_PYTHON_VERSION=3

RUN pip3 install --upgrade pip

RUN pip3 install jupyterlab==3.1.14 pyspark==3.1.1

COPY ./jars/ /opt/spark/jars

EXPOSE 8888
