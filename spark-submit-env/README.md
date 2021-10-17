# Local Spark Dev Env with Docker

Development environment for k8s.

Using a kubernetes image build to be ready for Azure Data Lake Storage Gen2 and Delta Lake.

## Start container

```bash
# In your local machine
docker-compose up -d --build
```

## Run spark-submit

```bash
# In your local machine
sh ./sh/run-spark-s.sh app.py
```

## Clean after work

```bash
# In your local machine
docker-compose down
```