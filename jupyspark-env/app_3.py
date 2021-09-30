# import libraries
from pyspark.sql import SparkSession

# main spark program
if __name__ == '__main__':

    # init spark session
    # name of the app
    spark = SparkSession \
            .builder \
            .appName("teste-3") \
            .getOrCreate()

    df = spark.read.format("com.crealytics.spark.excel").option("header", "true").load("airtravel.xlsx")
    
    df.printSchema()

    df.show()

    # stop spark session
    spark.stop()
