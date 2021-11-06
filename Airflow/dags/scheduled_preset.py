"""
Airflow DAG scheduled based on a preset value.
Author: Andrew Jarombek
Date: 11/3/2021
"""

from datetime import timedelta

import requests
from requests import Response
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


def get_bitcoin_price():
    response: Response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price: float = response.json().get('bpi').get('USD').get('rate_float')
    print(f'Bitcoin Price: {"${:,.2f}".format(price)}')


with DAG(
    dag_id="scheduled_preset",
    description="A DAG that is scheduled using a preset value",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval="@once",
    default_view="graph",
    is_paused_upon_creation=True,
    tags=["sample"]
) as dag:
    task = PythonOperator(task_id='python_task', python_callable=get_bitcoin_price)

    task
