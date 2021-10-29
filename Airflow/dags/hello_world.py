"""
Hello World Airflow DAG
Author: Andrew Jarombek
Date: 10/29/2021
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


def task():
    print(f"The current time is {datetime.now().strftime('%b. %d, %Y %-I:%M %p UTC')}")


with DAG(
    dag_id="hello_world",
    description="A hello world DAG which shows the basic execution flow of Airflow",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval=None,
    default_view="graph",
    tags=["sample"]
) as dag:
    bash_task = BashOperator(task_id='bash_task', bash_command='echo "Hello from Airflow!"')
    python_task = PythonOperator(task_id='python_task', python_callable=task)

    bash_task >> python_task
