# import libraries
from pyspark.sql import SparkSession

# main spark program
if __name__ == '__main__':

    # init spark session
    # name of the app
    spark = SparkSession \
            .builder \
            .appName("teste-2") \
            .getOrCreate()

    df = spark.read.csv("airtravel.csv", inferSchema=True, header=True)
    
    df.printSchema()

    df.show()

    # stop spark session
    spark.stop()
