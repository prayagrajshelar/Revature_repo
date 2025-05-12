from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryInsertJobOperator,
    BigQueryCreateEmptyDatasetOperator
)
from datetime import datetime

# Config
GCP_PROJECT = 'data-proc-project-457704'
BUCKET_NAME = 'prayagraj-bucket'
GCS_PATH = 'Bangalore_Indiranagar.csv'
BQ_DATASET = 'newdata'
BQ_RAW_TABLE = 'raw_branch_data'
BQ_CLEAN_TABLE = 'clean_branch_data'
BQ_RESULT_TABLE = 'info_extracted'

default_args = {
    'start_date': datetime(2025, 5, 12),
    'retries': 1,
}

with DAG('branch_data_cleaning_and_extraction',
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    start = DummyOperator(task_id='start')

    create_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_dataset',
        dataset_id=BQ_DATASET,
        project_id=GCP_PROJECT,
        location='US',
        exists_ok=True
    )

    load_csv = GCSToBigQueryOperator(
        task_id='load_raw_csv',
        bucket=BUCKET_NAME,
        source_objects=[GCS_PATH],
        destination_project_dataset_table=f'{GCP_PROJECT}.{BQ_DATASET}.{BQ_RAW_TABLE}',
        skip_leading_rows=1,
        source_format='CSV',
        write_disposition='WRITE_TRUNCATE',
        autodetect=True
    )

    clean_nulls = BigQueryInsertJobOperator(
        task_id='clean_null_values',
        configuration={
            "query": {
                "query": f"""
                    CREATE OR REPLACE TABLE `{GCP_PROJECT}.{BQ_DATASET}.{BQ_CLEAN_TABLE}` AS
                    SELECT * FROM `{GCP_PROJECT}.{BQ_DATASET}.{BQ_RAW_TABLE}`
                    WHERE FailureReason IS NOT NULL
                """,
                "useLegacySql": False
            }
        },
        location='US'
    )

    extract_info = BigQueryInsertJobOperator(
        task_id='extract_info',
        configuration={
            "query": {
                "query": f"""
                    CREATE OR REPLACE TABLE `{GCP_PROJECT}.{BQ_DATASET}.{BQ_RESULT_TABLE}` AS
                    SELECT FailureReason, COUNT(*) as count
                    FROM `{GCP_PROJECT}.{BQ_DATASET}.{BQ_CLEAN_TABLE}`
                    GROUP BY FailureReason
                    ORDER BY FailureReason DESC
                    LIMIT 5
                """,
                "useLegacySql": False
            }
        },
        location='US'
    )

    end = DummyOperator(task_id='finish')

    start >> create_dataset >> load_csv >> clean_nulls >> extract_info >> end
