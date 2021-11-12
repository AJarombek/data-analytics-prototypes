-- SQL command to add a ethereum price to the prices table.
-- Author: Andrew Jarombek
-- Date: 11/10/2021

INSERT INTO prices (
    coin, price, time
) VALUES (
    'ethereum', {{ params.price }}, {{ params.time }}
);