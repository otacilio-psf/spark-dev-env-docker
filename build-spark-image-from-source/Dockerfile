FROM otaciliopsf/spark-py:v3.1.1-hadoop3.2

USER root

RUN rm /opt/spark/jars/guava-14.0.1.jar

COPY ./jars/ /opt/spark/jars

USER 185