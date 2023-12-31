from datetime import timedelta, datetime
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Define common parameters
default_args = {
    "owner": "Servin",
    "retires": 5,
    "retry_delay": timedelta(minutes=5)

}

with DAG(
    dag_id="Postgres_airflow_connection_test_v01",
    default_args=default_args,
    description="First Airflow with Postgres connection",
    start_date=datetime(2023, 6, 17)
) as dag:

    create_weather_table = PostgresOperator(
        task_id="create_weather_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS master_weather (
            weather_id SERIAL PRIMARY KEY,
            forecast_date DATE NOT NULL,
            city VARCHAR NOT NULL,
            state VARCHAR NOT NULL,
            max_temp INTEGER NOT NULL,
            min_temp INTEGER NOT NULL);
          """
    )

    insert_weather_data = PostgresOperator(
        task_id="insert_weather_data",
        postgres_conn_id="postgres_localhost",
        sql="""
            INSERT INTO 
            master_weather(forecast_date, city, state, max_temp, min_temp) 
            VALUES 
                (CURRENT_DATE, 'Houston', 'TX', 101, 79),
                (CURRENT_DATE, 'Dallas', 'TX', 98, 75);
        """
    )

    create_weather_table >> insert_weather_data
