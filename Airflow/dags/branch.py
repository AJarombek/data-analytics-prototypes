"""
Airflow DAG with a branching task structure.
Author: Andrew Jarombek
Date: 11/12/2021
"""

from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago


def branch():
    pass


def weekend():
    pass


def weekday():
    pass


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


with DAG(
    dag_id="branch",
    description="A DAG that branches",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval="@daily",
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample", "branch"]
) as dag:
    branch_task = BranchPythonOperator(task_id='branch', python_callable=branch)
    weekend_task = PythonOperator(task_id='weekend_task', python_callable=weekend)
    weekday_task = PythonOperator(task_id='weekday_task', python_callable=weekday)

    branch_task >> [weekend_task, weekday_task]
