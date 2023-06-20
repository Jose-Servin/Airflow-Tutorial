from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
# Define common parameters
default_args = {
    "owner": "Servin",
    "retires": 5,
    "retry_delay": timedelta(minutes=5)

}


with DAG(
    dag_id="minio_sensor_v1",
    default_args=default_args,
    description="Simple Minio Bucket sensor",
    start_date=datetime(2023, 6, 20),
    schedule_interval="@daily"


) as dag:
    task_1 = S3KeySensor(
        task_id="minio_sensor_s3",
        bucket_name="airflow",
        bucket_key="data.csv",
        aws_conn_id="minio_conn"

    )

    task_1
