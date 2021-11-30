# Local Spark Dev Env with Docker

Development environment for kubernetes, spark-submit and jupyter notebook

Using a kubernetes image build to be ready for Azure Data Lake Storage Gen2 and Delta Lake.

You can create your own spark image from source, the tutorial is inside `build-spark-image-from-source`

## Options

You can choose to do your development on an interactive notebook with jupyter lab, run your script with spark-submit or submit your job to a local Kubernetes. 

* With spark submit `cd spark-submit-env`
    * Use the tutorial inside spark-submit-dev

* With Jupyter Lab `cd jupyspark-env`
    * Use the tutorial inside jupyspark-env

* With Kubernetes cluster `cd k8s`
    * Use the tutorial inside k8s
