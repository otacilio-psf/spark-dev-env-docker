# Local Spark Dev Env with Docker

Development environment for k8s.

Using the spark-operator image to ensure it will be the same environment.

## Start container

```bash
docker-compose up -d --build
```

## Run spark-submit

```bash
# In your local machine
sh ./sh/run-spark-s.sh app.py
```

## Clean after work

```bash
docker-compose down
```