if [ -z "$1" ]
then
      echo "Missing aplication path"
else
      docker exec -it jupyspark /opt/spark/bin/spark-submit $1
fi

