FROM otaciliopsf/spark-py:v3.1.1-hadoop3.2-abfss-delta

USER root

WORKDIR /opt/spark/work-dir

COPY app.py /opt/spark/work-dir

COPY ./jars/ /opt/spark/jars

USER 185