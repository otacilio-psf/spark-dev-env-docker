# import libraries
from pyspark.sql import SparkSession

# main spark program
if __name__ == '__main__':

    # init spark session
    # name of the app
    spark = SparkSession \
            .builder \
            .appName("teste-1") \
            .getOrCreate()

    data = [
        { "id": "1001", "type": "Regular" },
        { "id": "1002", "type": "Chocolate" },
        { "id": "1003", "type": "Blueberry" },
        { "id": "1004", "type": "Devil's Food" }
        ]

    df = spark.createDataFrame(data)
    
    df.printSchema()

    df.show()

    # stop spark session
    spark.stop()
