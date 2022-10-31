"""
Test code for python programs using Spark.
Author: Andrew Jarombek
Date: 10/10/2022
"""

import math
import os

import pytest
from pyspark.sql import DataFrame
import pyspark.sql.functions as F

from da_spark_prototypes.main import create_df, long_runs, order_by_mileage


@pytest.fixture()
def data() -> DataFrame:
    filename = os.path.join(
        os.path.dirname(__file__), "../../..", "data/exercises.json"
    )
    return create_df(filename)


def test_create_df(data: DataFrame):
    assert data.count() > 0


def test_long_runs(data: DataFrame):
    long_run_data = long_runs(data)
    assert long_run_data.count() == 2

    for row in long_run_data.collect():
        data = row.asDict()
        assert data.get('miles') >= 10


def test_order_by_mileage_asc(data: DataFrame):
    df = data.filter(F.col("type") == "kayak")
    assert df.count() > 0

    rows = order_by_mileage(df, desc=False).collect()
    prev = 0

    for row in rows:
        miles = row.miles
        assert miles >= prev
        prev = miles


def test_order_by_mileage_desc(data: DataFrame):
    df = data.filter(F.col("type") == "kayak")
    assert df.count() > 0

    rows = order_by_mileage(df).collect()
    prev = math.inf

    for row in rows:
        miles = row.miles
        assert miles <= prev
        prev = miles
