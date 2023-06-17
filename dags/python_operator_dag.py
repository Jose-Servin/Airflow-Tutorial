from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Define common parameters
default_args = {
    "owner": "Servin",
    "retires": 5,
    "retry_delay": timedelta(minutes=5)

}


def _greet(ti):
    first_name = ti.xcom_pull(task_ids="Returning_Baker", key="first_name")
    last_name = ti.xcom_pull(task_ids="Returning_Baker", key="last_name")
    age = ti.xcom_pull(task_ids="Returning_age", key="age")
    print(f"Hello, my name is {first_name} {last_name}, I am {age} years old!")


def _get_name(ti):
    ti.xcom_push(key="first_name", value="Baker")
    ti.xcom_push(key="last_name", value="Servin")


def _get_age(ti):
    ti.xcom_push(key="age", value=10)


with DAG(
    dag_id="python_dag_v6",
    default_args=default_args,
    description="First dag with a python operator.",
    start_date=datetime(2023, 6, 14),
    schedule_interval="@daily"
) as dag:
    task_1 = PythonOperator(
        task_id="Greet_with_Python",
        python_callable=_greet
    )

    task_2 = PythonOperator(
        task_id="Returning_Baker",
        python_callable=_get_name
    )

    task_3 = PythonOperator(
        task_id="Returning_age",
        python_callable=_get_age
    )

    [task_2, task_3] >> task_1
