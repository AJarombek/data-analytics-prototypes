import os
import glob
import importlib.util
from typing import List, Dict, Optional
from datetime import timedelta

import pytest

from airflow.models import DagBag, DAG
from airflow.utils.dag_cycle_tester import check_cycle

dag_dir = os.path.join(os.path.dirname(__file__), "../dags")
dag_path = os.path.join(dag_dir, '*.py')
dag_files = glob.glob(dag_path)


def get_dag_bag(dag_folder: str) -> DagBag:
    return DagBag(dag_folder=dag_folder, include_examples=False)


def get_dag(dag_id) -> DAG:
    dag_bag = get_dag_bag(dag_dir)
    return dag_bag.dags.get(dag_id)


def check_no_cycles(dag_file: str, path: str) -> None:
    module_name, _ = os.path.splitext(dag_file)
    module_path = os.path.join(path, dag_file)
    mod_spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(mod_spec)

    mod_spec.loader.exec_module(module)

    dag_objects = [var for var in vars(module).values() if isinstance(var, DAG)]

    for dag in dag_objects:
        check_cycle(dag)


def check_dag_dependencies(
    dag: DAG, task_id: str, expected_upstream_tasks: List[str], expected_downstream_tasks: List[str]
) -> None:
    task = dag.get_task(task_id)

    actual_upstream_tasks = [task.task_id for task in task.upstream_list]
    actual_downstream_tasks = [task.task_id for task in task.downstream_list]
    assert sorted(actual_upstream_tasks) == sorted(expected_upstream_tasks)
    assert sorted(actual_downstream_tasks) == sorted(expected_downstream_tasks)


def check_dag_schedules(dag_bag: DagBag, schedules: Dict[str, Optional[str]]) -> None:
    for dag_id, schedule in schedules.items():
        dag = dag_bag.dags.get(dag_id)

        if schedule is None:
            assert dag.schedule_interval is None
        else:
            assert dag.schedule_interval == schedule


def test_no_import_errors() -> None:
    dag_bag = get_dag_bag(dag_dir)
    assert len(dag_bag.import_errors) == 0, "DAGs have import errors"


@pytest.mark.parametrize("dag_file", dag_files)
def test_dag_integrity(dag_file: str) -> None:
    check_no_cycles(dag_file, dag_path)


def test_expected_dags() -> None:
    dag_bag = get_dag_bag(dag_dir)
    assert len(dag_bag.dags) == 9
    assert sorted(dag_bag.dag_ids) == [
        'branch',
        'fan_in_out',
        'hello_world',
        'scheduled_cron',
        'scheduled_frequency',
        'scheduled_preset',
        'taskflow',
        'trigger_rule_none_failed',
        'xcom'
    ]


def test_proper_schedules() -> None:
    dag_bag = get_dag_bag(dag_dir)

    schedules = {
        'branch': '@daily',
        'fan_in_out': '@once',
        'hello_world': None,
        'scheduled_cron': '@once',
        'scheduled_frequency': timedelta(hours=12),
        'scheduled_preset': '@once',
        'taskflow': '@daily',
        'trigger_rule_none_failed': '@daily',
        'xcom': '@daily'
    }

    check_dag_schedules(dag_bag, schedules)


def test_dags_contain_tasks() -> None:
    dag_bag = get_dag_bag(dag_dir)

    tasks_dict = {
        'branch': ['branch', 'weekend_task', 'weekday_task'],
        'fan_in_out': [
            'create_table_task',
            'get_bitcoin_price_task',
            'insert_bitcoin_task',
            'get_ethereum_price_task',
            'insert_ethereum_task',
            'select_prices_task'
        ],
        'hello_world': ['bash_task', 'python_task'],
        'scheduled_cron': ['python_task'],
        'scheduled_frequency': ['python_task'],
        'scheduled_preset': ['python_task'],
        'taskflow': ['data_creation', 'data_cleaning', 'data_analysis'],
        'trigger_rule_none_failed': ['branch', 'standard_time_task', 'daylight_savings_task', 'always_task'],
        'xcom': ['data_creation_task', 'data_cleaning_task', 'data_analysis_task']
    }

    for dag_id, expected_tasks in tasks_dict.items():
        dag = dag_bag.dags.get(dag_id)
        actual_tasks_objects = dag.tasks
        actual_tasks = [task.task_id for task in actual_tasks_objects]
        assert actual_tasks == expected_tasks


def test_branch_task_dependencies() -> None:
    dag = get_dag('branch')

    check_dag_dependencies(
        dag=dag,
        task_id='branch',
        expected_upstream_tasks=[],
        expected_downstream_tasks=['weekend_task', 'weekday_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='weekend_task',
        expected_upstream_tasks=['branch'],
        expected_downstream_tasks=[]
    )

    check_dag_dependencies(
        dag=dag,
        task_id='weekday_task',
        expected_upstream_tasks=['branch'],
        expected_downstream_tasks=[]
    )


def test_fan_in_out_task_dependencies() -> None:
    dag = get_dag('fan_in_out')

    check_dag_dependencies(
        dag=dag,
        task_id='create_table_task',
        expected_upstream_tasks=[],
        expected_downstream_tasks=['get_bitcoin_price_task', 'get_ethereum_price_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='get_bitcoin_price_task',
        expected_upstream_tasks=['create_table_task'],
        expected_downstream_tasks=['insert_bitcoin_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='insert_bitcoin_task',
        expected_upstream_tasks=['get_bitcoin_price_task'],
        expected_downstream_tasks=['select_prices_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='get_ethereum_price_task',
        expected_upstream_tasks=['create_table_task'],
        expected_downstream_tasks=['insert_ethereum_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='insert_ethereum_task',
        expected_upstream_tasks=['get_ethereum_price_task'],
        expected_downstream_tasks=['select_prices_task']
    )

    check_dag_dependencies(
        dag=dag,
        task_id='select_prices_task',
        expected_upstream_tasks=['insert_bitcoin_task', 'insert_ethereum_task'],
        expected_downstream_tasks=[]
    )
