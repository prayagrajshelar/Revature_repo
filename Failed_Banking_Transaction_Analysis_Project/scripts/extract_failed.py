from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower

# Create Spark session
spark = SparkSession.builder.appName("FilterFailedTransactions").getOrCreate()

# Load cleaned transactions CSV from GCS
df = spark.read.option("header", True).csv("gs://prayagraj-bucket/processed/cleaned_transactions.csv/*.csv")

# Normalize status column and filter for failed transactions
df_failed = df.filter(lower(col("Status")) == "failed")

# Write to Cloud SQL (MySQL)
jdbc_url = "jdbc:mysql://34.59.34.192:3306/workdb"
properties = {
    "user": "prayagraj",
    "password": "root",
    "driver": "com.mysql.cj.jdbc.Driver"
}

df_failed.write.jdbc(url=jdbc_url, table="failed_transactions", mode="overwrite", properties=properties)

spark.stop()
