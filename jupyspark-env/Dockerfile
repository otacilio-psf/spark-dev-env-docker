FROM gcr.io/spark-operator/spark-py:v3.1.1

USER root:root

RUN pip install jupyterlab==3.1.14 pyspark==3.1.1 findspark==1.4.2

COPY ./jars/ /opt/spark/jars

EXPOSE 8888
