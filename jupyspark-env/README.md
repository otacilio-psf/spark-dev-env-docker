# Local JupySpark Dev Env with Docker

Development environment for k8s with jupyter lab.

Using the spark-operator image to ensure it will be the same environment.

## Start container

```bash
docker-compose up -d
# if you have change something in the Dockerfile
docker-compose up -d --build
```

## Access JupyterLab via the link


> [http://localhost:8888/lab](http://localhost:8888/lab)


## Converting notebook to python script

```bash
# In your local machine
sh ./sh/notebook-to-py.sh app.ipynb
```

## Run with spark-submit

```bash
# In your local machine
sh ./sh/run-spark-s.sh app.py
```

## Clean after work

```bash
docker-compose down
```