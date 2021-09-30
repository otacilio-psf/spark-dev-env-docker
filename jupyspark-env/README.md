# Local Spark Dev Env with Docker

Development environment for k8s.

Using the spark-operator image to ensure it will be the same environment.

## Start container

```bash
docker-compose up -d
```

## Copy dependencies jars

```bash
docker cp jars/. spark:/opt/spark/jars
```

## Create a local alias for spark-submit

```bash
alias spark-s="docker exec -it spark /opt/spark/bin/spark-submit"
```

## Run exemple

```bash
spark-s app_3.py
```

## Clean after work

```bash
docker-compose down
```