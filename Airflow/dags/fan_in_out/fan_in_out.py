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

from fan_in_out.utils import get_ethereum_price, get_bitcoin_price


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
        sql='sql/create_price_table.sql'
    )

    get_bitcoin_price_task = PythonOperator(task_id='get_bitcoin_price_task', python_callable=get_bitcoin_price)

    insert_bitcoin_task = PostgresOperator(
        task_id='insert_bitcoin_task',
        postgres_conn_id='postgres_default',
        sql='sql/insert_bitcoin_price.sql',
        parameters={
            'price': '{{ti.xcom_pull(task_ids="get_bitcoin_price_task", key="return_value")}}',
            'time': '{{ts}}'
        }
    )

    get_ethereum_price_task = PythonOperator(task_id='get_ethereum_price_task', python_callable=get_ethereum_price)

    insert_ethereum_task = PostgresOperator(
        task_id='insert_ethereum_task',
        postgres_conn_id='postgres_default',
        sql='fan_in_out/insert_ethereum_price.sql',
        parameters={
            'price': '{{ti.xcom_pull(task_ids="get_ethereum_price_task", key="return_value")}}',
            'time': '{{ts}}'
        }
    )

    select_prices_task = PostgresOperator(
        task_id='select_prices_task',
        postgres_conn_id='postgres_default',
        sql='sql/select_prices.sql'
    )

    create_table_task >> [get_bitcoin_price_task, get_ethereum_price_task]
    get_bitcoin_price_task >> insert_bitcoin_task >> select_prices_task
    get_ethereum_price_task >> insert_ethereum_task >> select_prices_task
