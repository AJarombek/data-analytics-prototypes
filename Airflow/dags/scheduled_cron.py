"""
Airflow DAG with a cron schedule.
Author: Andrew Jarombek
Date: 11/6/2021
"""

from typing import List, Dict, Union
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


def get_ethereum_price():
    response: Response = requests.get('https://api2.binance.com/api/v3/ticker/24hr')
    eth_info: List[Dict[str, Union[str, int]]] = [item for item in response.json() if item.get('symbol') == 'ETHUSDT']

    if len(eth_info) == 0:
        print(f"Ethereum Price Not Found")
    else:
        price = "${:,.2f}".format(eth_info[0].get('lastPrice'))
        print(f"Ethereum Price: {price}")


with DAG(
    dag_id="scheduled_cron",
    description="A DAG that has a cron schedule",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval="@once",
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample"]
) as dag:
    task = PythonOperator(task_id='python_task', python_callable=get_ethereum_price)

    task