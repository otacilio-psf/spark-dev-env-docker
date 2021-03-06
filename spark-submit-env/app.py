from pyspark.sql import SparkSession
import os
import time

class SparkJob:
    storage_name = "mystgaccount"
    container_name = "mycontainer"
    path = f"abfss://{container_name}@{storage_name}.dfs.core.windows.net/"
    source = "airtravel.xlsx"
    target = f"delta/bronze/airtravel/{int(time.time())}"

    def _spark_session(self):
        print("======================= SparkSession Starting ========================")
        self.spark = SparkSession.builder.appName("job-example").getOrCreate()
        print("=========================== Set Spark Conf ===========================")
        self.spark.conf.set(f"fs.azure.account.auth.type.{self.storage_name}.dfs.core.windows.net", "OAuth" )
        self.spark.conf.set(f"fs.azure.account.oauth.provider.type.{self.storage_name}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
        self.spark.conf.set(f"fs.azure.account.oauth2.client.id.{self.storage_name}.dfs.core.windows.net", os.getenv('AZURE_CLIENT_ID'))
        self.spark.conf.set(f"fs.azure.account.oauth2.client.secret.{self.storage_name}.dfs.core.windows.net", os.getenv('AZURE_CLIENT_SECRET'))
        self.spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{self.storage_name}.dfs.core.windows.net", f"https://login.microsoftonline.com/{os.getenv('AZURE_TENANT_ID')}/oauth2/token")
        self.spark.conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        self.spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        
    def _read_data(self):
        print("============================== Read data =============================")
        self.df = self.spark.read.format("com.crealytics.spark.excel").option("header", "true").load(self.source)
        self.df.printSchema()
        self.df.show()

    def _write_data(self):
        print("============================= Write data =============================")
        self.df.write.mode("overwrite").format("delta").save(self.path+self.target)

    def process(self):
        self._spark_session()
        self._read_data()
        self._write_data()
        print("============================== Finished ==============================")
        self.spark.stop()

if __name__ == "__main__":
    sj = SparkJob()
    sj.process()
