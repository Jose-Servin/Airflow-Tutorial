from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


# Define common parameters
default_args = {
    "owner": "Servin",
    "retires": 5,
    "retry_delay": timedelta(minutes=2)

}

with DAG(
    dag_id="first_dag_v4",
    default_args=default_args,
    description="First test dag built",
    start_date=datetime(2023, 6, 13),
    schedule_interval="@daily"
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello world!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo This is from the second task!"
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo This third task will run at the same time as task2."
    )

    task1 >> [task2, task3]
