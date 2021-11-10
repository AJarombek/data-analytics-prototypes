-- SQL command to create a table for cypto prices.  Used by an Airflow DAG.
-- Author: Andrew Jarombek
-- Date: 11/9/2021

CREATE TABLE IF NOT EXISTS prices (
    coin VARCHAR(30) NOT NULL,
    price DECIMAL NOT NULL,
    time TIMESTAMP NOT NULL
);