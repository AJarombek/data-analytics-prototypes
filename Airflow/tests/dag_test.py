import os
import glob
import importlib.util

import pytest

from airflow.models import DagBag, DAG
from airflow.utils.dag_cycle_tester import check_cycle

dag_dir = os.path.join(os.path.dirname(__file__), "../dags")
dag_path = os.path.join(dag_dir, '*.py')
dag_files = glob.glob(dag_path)


def get_dag_bag(dag_folder: str) -> DagBag:
    return DagBag(dag_folder=dag_folder, include_examples=False)


def check_no_cycles(dag_file: str, path: str) -> None:
    module_name, _ = os.path.splitext(dag_file)
    module_path = os.path.join(path, dag_file)
    mod_spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(mod_spec)

    mod_spec.loader.exec_module(module)

    dag_objects = [var for var in vars(module).values() if isinstance(var, DAG)]

    for dag in dag_objects:
        check_cycle(dag)


def test_no_import_errors():
    dag_bag = get_dag_bag(dag_dir)
    assert len(dag_bag.import_errors) == 0, "DAGs have import errors"


@pytest.mark.parametrize("dag_file", dag_files)
def test_dag_integrity(dag_file):
    check_no_cycles(dag_file, dag_path)


def test_expected_dags():
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


def test_proper_schedules():
    pass


def test_dags_contain_tasks():
    pass


def test_branch_task_dependencies():
    pass
