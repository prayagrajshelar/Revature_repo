
# Failed Banking Transaction Analysis

This project processes daily bank transaction data using GCP tools.

## Pipeline:
1. Upload CSVs and python files to GCS bucket.
gsutil mb gs://bucket-name/
gsutil cp source-location/*.py gs://bucket-name/scripts/

2. Create Cluster in GCP 
gcloud dataproc clusters create cluster-name --region=us-central1 --zone=us-central1-a --single-node --master-machine-type=n1-standard-2 --image-version=2.0-debian10

3. Clean and merge data using PySpark on Dataproc.
gcloud dataproc jobs submit pyspark gs://bucket-name/scripts/clean_data.py --cluster=cluster-name --region=us-central1

4. Create MYSQL instance in cloud
5. Add Network Connection in MySQL instance
6. Create new User and new database in Mysql instance


7. Extract failed transactions and load them into Cloud SQL (MySQL).  (By executing the python file)
gcloud dataproc jobs submit pyspark gs://bucket-name/scripts/extract_details.py --cluster=cluster-name --region=us-central1

8. create Bigquery dataset (Must be having same Region as Mysql Instance)
9. Make connection to Mysql Database Using BigQuery Federation Service
    {
        go to -> Add dataset -> Select Database -> Search For Mysql -> Select Federation in left panel -> select Bigquery Federation
        and fill feilds and create connection
        go to connection copy second last address and go to IAM for assignig some roles
        in IAM click "+Grant Access" and paste that address of conncetion and add Roles:
            BigQuery Admin
            BigQuery Conncetion User
            Bigquery Connection Admin
            Cloud Sql Client
            Dataproc Worker
    }

10. Now you have successfully connected to mysql database
11. Take Filtered Data from mysql table and store it in BigQuery table
Query:
    CREATE OR REPLACE TABLE data-proc-project-457704.mydataset.failed_transactions AS
    SELECT *
    FROM EXTERNAL_QUERY(
    "data-proc-project-457704.us-central1.myconnection"
    "SELECT * FROM workdb.failed_transactions"
    )
12. Perform some SQL queries on that Bigquery table and Open the Result in Looker Table

## Folder Structure:
- data/: Contains sample CSVs for 3 cities × 5 branches.
- scripts/: PySpark scripts to clean and extract data.
