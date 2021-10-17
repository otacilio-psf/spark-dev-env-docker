if [ -z "$1" ]
then
      echo "Missing notebook path"
else
      docker exec -it jupyspark jupyter nbconvert $1 --to script
fi

