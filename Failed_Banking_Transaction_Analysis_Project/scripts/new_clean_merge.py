from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim

# Create Spark session
spark = SparkSession.builder.appName("CleanAndMergeAllTransactions").getOrCreate()

# Load CSV files from GCS bucket
df = spark.read.csv("gs://prayagraj-bucket/data/*.csv", header=True, inferSchema=True)

# Clean column names (remove leading/trailing spaces)
for col_name in df.columns:
    df = df.withColumnRenamed(col_name, col_name.strip())

# Clean data values (trim whitespaces from values)
for col_name in df.columns:
    df = df.withColumn(col_name, trim(col(col_name)))

# Drop rows with nulls
df_clean = df.na.drop()

# Filter out empty TransactionID
df_clean = df_clean.filter(col("TransactionID") != "")

# Write cleaned full transaction data to output location
df_clean.write.csv("gs://prayagraj-bucket/processed/cleaned_transactions.csv", header=True, mode='overwrite')

spark.stop()
