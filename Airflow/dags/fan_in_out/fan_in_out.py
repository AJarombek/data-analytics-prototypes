"""
Airflow DAG with a 'fan in' and 'fan out' task structure.
Author: Andrew Jarombek
Date: 11/10/2021
"""

from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


with DAG(
    dag_id="fan_in_out",
    description="A DAG that fans in and out",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval="@once",
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample", "postgres"]
) as dag:
    create_table_task = PostgresOperator(
        task_id='create_table_task',
        postgres_conn_id='postgres_default',
        sql='fan_in_out/create_price_table.sql'
    )

    bitcoin_task = PostgresOperator(
        task_id='bitcoin_task',
        postgres_conn_id='postgres_default',
        sql='fan_in_out/insert_bitcoin_price.sql',
        parameters={'price': '', 'time': ''}
    )

    ethereum_task = PostgresOperator(
        task_id='ethereum_task',
        postgres_conn_id='postgres_default',
        sql='fan_in_out/insert_ethereum_price.sql',
        parameters={'price': '', 'time': ''}
    )

    select_prices_task = PostgresOperator(
        task_id='select_prices_task',
        postgres_conn_id='postgres_default',
        sql='fan_in_out/select_prices.sql'
    )

    create_table_task >> [bitcoin_task, ethereum_task]
    bitcoin_task >> select_prices_task
    ethereum_task >> select_prices_task
