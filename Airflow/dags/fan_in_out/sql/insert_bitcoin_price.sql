-- SQL command to add a bitcoin price to the prices table.
-- Author: Andrew Jarombek
-- Date: 11/10/2021

INSERT INTO prices (
    coin, price, time
) VALUES (
    'bitcoin', {{ti.xcom_pull(task_ids="get_bitcoin_price_task", key="return_value")}}, '{{ts}}'
);