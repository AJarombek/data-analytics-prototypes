-- SQL command to add a bitcoin price to the prices table.
-- Author: Andrew Jarombek
-- Date: 11/10/2021

INSERT INTO prices (
    coin, price, time
) VALUES (
    'bitcoin', {{ params.price }}, {{ params.time }}
);