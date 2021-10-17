# Developing enviroment with Kubernetes

Using a kubernetes image build to be ready for Azure Data Lake Storage Gen2 and Delta Lake.

# Creating k8s cluster with k3d

[Install k3d](https://k3d.io/v5.0.1/#installation)

[Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

```
k3d cluster create --config manifests/cluster-k3d.yaml

kubectl config use-context k3d-spark-cluster
```

# Config k8s

## Namespace

```
kubectl create namespace spark-job
```

## Secrets

Export the env variables first in your local machine

```
kubectl create secret generic job-example \
    --from-literal=AZURE_CLIENT_ID=$AZURE_CLIENT_ID \
    --from-literal=AZURE_CLIENT_SECRET=$AZURE_CLIENT_SECRET \
    --from-literal=AZURE_TENANT_ID=$AZURE_TENANT_ID \
    --namespace spark-job
```

or

```
kubectl create secret generic job-example \
    --from-env-file=/.env
    --namespace spark-job
```

## Role bing

```
kubectl apply -f manifests/crb-spark.yaml --namespace spark-job
```

## SparkOperator

[Install Helm](https://helm.sh/docs/intro/install/)

```
helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

helm repo update

helm install spark spark-operator/spark-operator --set image.tag=v1beta2-1.2.3-3.1.1 --namespace spark-job --set webhook.enable=true
```

# Spark job

## Building job image

Change the MyRepository to your docker hub account
* Is necessary to change the job manifest too

```
spec:
  image: "MyRepository/spark-py:job-example"
```

After change run

```
docker build . -t MyRepository/spark-py:job-example

docker push MyRepository/spark-py:job-example
```

## Submit job

```
kubectl apply -f manifests/job-spark-exaple.yaml --namespace spark-job
```

## Monitoring

3 options

```
kubectl get sparkapplications job-example --namespace spark-job
```
```
kubectl logs --follow pod/job-example-driver --namespace spark-job
```
```
kubectl get all --namespace spark-job
```

> hint: you can use `watch 'kubectl get all --namespace spark-job'`

# Cleaning

```
kubectl delete SparkApplication job-example --namespace spark-job

kubectl delete clusterrolebinding crb-spark

helm uninstall spark --namespace spark-job

kubectl delete namespace spark-job

k3d cluster delete spark-cluster
```