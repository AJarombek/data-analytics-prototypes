-- SQL command to add a ethereum price to the prices table.
-- Author: Andrew Jarombek
-- Date: 11/10/2021

INSERT INTO prices (
    coin, price, time
) VALUES (
    'ethereum', {{ti.xcom_pull(task_ids="get_ethereum_price_task", key="return_value")}}, '{{ts}}'
);