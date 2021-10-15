if [ -z "$1" ]
then
      echo "Missing application path"
else
      docker exec -it spark /opt/spark/bin/spark-submit $1
fi

