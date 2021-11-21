"""
Airflow DAG with a task using the trigger rule 'none_failed'.
Author: Andrew Jarombek
Date: 11/13/2021
"""

from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago


def branch():
    if datetime.now().dst() == 0:
        return 'standard_time_task'
    else:
        return 'daylight_savings_task'


def standard_time():
    print("Lily the bear is awake")


def daylight_savings():
    print("Lily the bear is hibernating")


def always():
    print("Lily is in NYC")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


with DAG(
    dag_id="trigger_rule_none_failed",
    description="A DAG that has a task using the none_failed trigger rule",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval="@daily",
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample", "branch", "python"]
) as dag:
    branch_task = BranchPythonOperator(task_id='branch', python_callable=branch)
    standard_time_task = PythonOperator(task_id='standard_time_task', python_callable=standard_time)
    daylight_savings_task = PythonOperator(task_id='daylight_savings_task', python_callable=daylight_savings)
    always_task = PythonOperator(task_id='always_task', python_callable=always, trigger_rule='none_failed')

    branch_task >> [standard_time_task, daylight_savings_task]
    standard_time_task >> always_task
    daylight_savings_task >> always_task
