from pyspark.sql import SparkSession

class SparkJob:

    def _spark_session(self):
        print("======================= SparkSession Starting ========================")
        self.spark = SparkSession.builder.appName("job-example").getOrCreate()
        print("=========================== Set Spark Conf ===========================")
        #self.spark.conf.set('key', 'value')

    def _read_data(self):
        print("============================== Read data =============================")
        self.df = self.spark.read.format("com.crealytics.spark.excel").option("header", "true").load("airtravel.xlsx")
        self.df.printSchema()
        self.df.show()

    def _write_data(self):
        print("============================= Write data =============================")
        self.df.write.mode("overwrite").format("delta").save("delta/airtravel")

    def process(self):
        self._spark_session()
        self._read_data()
        self._write_data()
        print("============================== Finished ==============================")
        self.spark.stop()

if __name__ == "__main__":
    sj = SparkJob()
    sj.process()
