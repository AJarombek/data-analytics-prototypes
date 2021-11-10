"""
Airflow DAG with a frequency schedule.
Author: Andrew Jarombek
Date: 11/9/2021
"""

from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from utils import get_bitcoin_price


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


with DAG(
    dag_id="scheduled_frequency",
    description="A DAG that has a frequency schedule",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval=timedelta(hours=12),
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample"]
) as dag:
    task = PythonOperator(task_id='python_task', python_callable=get_bitcoin_price)

    task