"""
Airflow DAG with a branching task structure.
Author: Andrew Jarombek
Date: 11/12/2021
"""

from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.utils.dates import days_ago


def branch():
    if datetime.now().weekday() >= 5:
        return 'weekend_task'
    else:
        return 'weekday_task'


def weekend():
    print(
        "Schedule:\n"
        "8 AM - 12 PM: Run & Workout\n"
        "12 PM - 10 PM: Code & Relax"
    )


def weekday():
    print(
        "Schedule:\n"
        "6 AM - 9 AM: Run & Workout\n"
        "9 AM - 5 PM: Work\n"
        "5 PM - 10 PM: Code & Relax"
    )


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
    tags=["sample", "branch", "python"]
) as dag:
    branch_task = BranchPythonOperator(task_id='branch', python_callable=branch)
    weekend_task = PythonOperator(task_id='weekend_task', python_callable=weekend)
    weekday_task = PythonOperator(task_id='weekday_task', python_callable=weekday)

    branch_task >> [weekend_task, weekday_task]
