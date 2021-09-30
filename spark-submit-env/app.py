from pyspark.sql import SparkSession

if __name__ == '__main__':

    spark = SparkSession \
            .builder \
            .appName("Sample") \
            .getOrCreate()

    df = spark.read.format("com.crealytics.spark.excel").option("header", "true").load("airtravel.xlsx")
    
    df.printSchema()

    df.show()

    spark.stop()
