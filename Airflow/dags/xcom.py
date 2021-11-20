"""
Airflow DAG that uses XCOMs to send data between tasks.
Author: Andrew Jarombek
Date: 11/14/2021
"""

from typing import Dict, Any
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.models.taskinstance import TaskInstance
import pandas as pd


def data_creation():
    return {
        'dates': ['11/07/2021', '11/13/2021', '11/15/2021', '11/16/2021', '11/17/2021', '11/19/2021'],
        'miles': [26.2, 2.25, 2.96, 4.5, 5.26, 6],
        'location': ['New York, NY', 'Riverside, CT', 'New York, NY', 'New York, NY', 'New York, NY', 'New York, NY'],
        'time': ['2:49:25', '16:18', '21:11', '32:46', '38:03', '43:23']
    }


def data_cleaning(**context):
    ti: TaskInstance = context["ti"]
    running_dict: Dict[str, Any] = ti.xcom_pull(task_ids='data_creation_task', key='return_value')
    df = pd.DataFrame(running_dict)

    filtered_df = df[(df['miles'] < 26.2) & (df['location'] != 'Riverside, CT')]
    return filtered_df.to_dict()


def data_analysis(data):
    df = pd.DataFrame(data)
    print(f"Average Run Length in Miles: {df.mean()['miles']}")


default_args = {
    'owner': 'airflow',
    'depends_on_past': False
}


with DAG(
    dag_id="xcom",
    description="A DAG that uses XCOMs to send data between tasks",
    default_args=default_args,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval=None,
    default_view="graph",
    is_paused_upon_creation=False,
    tags=["sample", "python"]
) as dag:
    data_creation_task = PythonOperator(task_id='data_creation_task', python_callable=data_creation)
    data_cleaning_task = PythonOperator(task_id='data_cleaning_task', python_callable=data_cleaning)
    data_analysis_task = PythonOperator(
        task_id='data_analysis_task',
        python_callable=data_analysis,
        templates_dict={"data": "{{ti.xcom_pull(task_ids='data_creation_task', key='return_value')}}"}
    )

    data_creation_task >> data_cleaning_task >> data_analysis_task
