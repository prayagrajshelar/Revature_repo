from airflow import models
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

# DAG definition
default_args = {
    'start_date': datetime(2024, 1, 1),
}

with models.DAG(
    dag_id='gcs_to_bigquery_pipeline',
    default_args=default_args,
    schedule_interval=None,  # manual trigger
    catchup=False,
) as dag:

    # Task 1: Load CSV from GCS to BigQuery
    load_csv = GCSToBigQueryOperator(
        task_id='load_csv_to_bq',
        bucket='prayagraj-bucket',
        source_objects=['sample_data.csv'],
        destination_project_dataset_table='data-proc-project-457704.newdataset.people',
        schema_fields=[
            {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
            {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
            {'name': 'age', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        ],
        write_disposition='WRITE_TRUNCATE',
        skip_leading_rows=1,
        source_format='CSV',
    )

    # Task 2: Run a BigQuery SQL job
    query_job = BigQueryInsertJobOperator(
        task_id="run_bigquery_sql",
        configuration={
            "query": {
                "query": "SELECT name, age FROM data-proc-project-457704.newdataset.people WHERE age > 28",
                "useLegacySql": False,
            }
        },
    )

    load_csv >> query_job