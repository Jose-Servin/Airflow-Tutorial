from datetime import timedelta, datetime
from typing import Dict
from airflow.decorators import dag, task

# Define common parameters
default_args = {
    "owner": "Servin",
    "retires": 5,
    "retry_delay": timedelta(minutes=5)

}


@dag(
    dag_id="task_flow_api_v1",
    default_args=default_args,
    description="First dag built with the taskflow API",
    start_date=datetime(2023, 6, 16),
    schedule_interval="@daily"
)
def hello_dag():
    """
    Simple TaskFlowAPI Dag.

    Returns:
        None
    """
    @task
    def _get_name() -> Dict[str, str]:
        return {
            'first_name': 'Baker',
            'last_name': 'Servin'
        }

    @task
    def _get_age():
        return 19

    @task
    def greet(first_name, last_name, age):
        print(
            f"Hello world, my name is {first_name} {last_name} and I am {age} years old! ")

    name_dict = _get_name()
    age = _get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'], age=age)


hello_dag = hello_dag()
