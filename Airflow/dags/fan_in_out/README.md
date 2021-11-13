### Overview

Files used in an Airflow DAG which has tasks that fan-in and fan-out.

### Files

| Filename                 | Description                                                                            |
|--------------------------|----------------------------------------------------------------------------------------|
| `fan_in_out.py`          | The Airflow DAG file.                                                                  |
| `utils.py`               | Utility functions used by the Airflow DAG.                                             |
| `sql`                    | Directory containing SQL files used by the `PostgresOperator` tasks in the DAG.        |
