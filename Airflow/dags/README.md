### Overview

Python DAG files loaded onto the Airflow server.

### Files

| Filename                      | Description                                                                       |
|-------------------------------|-----------------------------------------------------------------------------------|
| `fan_in_out`                  | Code for a DAG that has tasks which fan-in and fan-out.                           |
| `branch.py`                   | Airflow DAG that has branching tasks.                                             |
| `hello_world.py`              | Hello World Airflow DAG.                                                          |
| `scheduled_cron.py`           | Airflow DAG which has a cron schedule.                                            |
| `scheduled_frequency.py`      | Airflow DAG which is scheduled based on a frequency.                              |
| `scheduled_preset.py`         | Airflow DAG which is scheduled based on a preset value.                           |
| `taskflow.py`                 | Airflow DAG which uses the Taskflow API.                                          |
| `trigger_rule_none_failed.py` | Airflow DAG which has a task with the `none_failed` trigger rule.                 |
| `utils.py`                    | Utility functions used by the Airflow DAGs.                                       |
| `xcom.py`                     | Airflow DAG which uses XCOMs to share data between tasks.                         |
