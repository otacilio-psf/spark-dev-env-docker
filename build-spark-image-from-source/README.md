# Building your own Spark image

```
wget https://archive.apache.org/dist/spark/spark-3.1.1/spark-3.1.1-bin-hadoop3.2.tgz

tar xvzf spark-3.1.1-bin-hadoop3.2.tgz

rm spark-3.1.1-bin-hadoop3.2.tgz

cd spark-3.1.1-bin-hadoop3.2

./bin/docker-image-tool.sh -r otaciliopsf -t v3.1.1-hadoop3.2 -p kubernetes/dockerfiles/spark/bindings/python/Dockerfile build

docker push otaciliopsf/spark:v3.1.1-hadoop3.2

docker push otaciliopsf/spark-py:v3.1.1-hadoop3.2

# To add your dependencies, place them inside the jars folder and continue following the steps

cd ..

docker build . -t otaciliopsf/spark-py:v3.1.1-hadoop3.2-abfss-delta

docker push otaciliopsf/spark-py:v3.1.1-hadoop3.2-abfss-delta
```
