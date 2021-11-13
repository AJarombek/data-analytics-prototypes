### Overview

SQL files used by the `fan_in_out` Airflow DAG.  These files are used by the `PostgresOperator` tasks.

### Files

| Filename                    | Description                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------|
| `create_price_table.sql`    | Create table `prices` statement.                                                       |
| `insert_bitcoin_price.sql`  | Insert statement for a Bitcoin price.  This SQL statement is templated for Airflow.    |
| `insert_ethereum_price.sql` | Insert statement for an Ethereum price.  This SQL statement is templated for Airflow.  |
| `select_prices.sql`         | Select statement for the `prices` table.                                               |
