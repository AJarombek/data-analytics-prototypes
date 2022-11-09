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

from da_spark_prototypes.main import (
    create_df,
    long_runs,
    order_by_mileage,
    walk_intensity,
    create_exercise_type_table,
    create_languages_table,
    sum_recent_years,
    grouped_exercise_mileage,
)


@pytest.fixture()
def data() -> DataFrame:
    filename = os.path.join(
        os.path.dirname(__file__), "../../..", "data/exercises.json"
    )
    return create_df(filename)


def test_create_df(data: DataFrame) -> None:
    assert data.count() > 0


def test_long_runs(data: DataFrame) -> None:
    long_run_data = long_runs(data)
    assert long_run_data.count() == 2

    for row in long_run_data.collect():
        data = row.asDict()
        assert data.get('miles') >= 10


def test_order_by_mileage_asc(data: DataFrame) -> None:
    df = data.filter(F.col("type") == "kayak")
    assert df.count() > 0

    rows = order_by_mileage(df, desc=False).collect()
    prev = 0

    for row in rows:
        miles = row.miles
        assert miles >= prev
        prev = miles


def test_order_by_mileage_desc(data: DataFrame) -> None:
    df = data.filter(F.col("type") == "kayak")
    assert df.count() > 0

    rows = order_by_mileage(df).collect()
    prev = math.inf

    for row in rows:
        miles = row.miles
        assert miles <= prev
        prev = miles


def test_walk_intensity(data: DataFrame) -> None:
    rows = walk_intensity(data).collect()
    assert len(rows) == 5

    for row in rows:
        assert row.intensity >= 1


def test_grouped_mileage(data: DataFrame) -> None:
    df = grouped_exercise_mileage(data)
    first = df.first().asDict()
    assert first.get('type') == 'virtual bike'


def test_create_exercise_type_table() -> None:
    df = create_exercise_type_table()
    assert df.count() == 9


def test_create_languages_table() -> None:
    df = create_languages_table()
    assert df.count() == 5


def test_sum_recent_years() -> None:
    df = sum_recent_years()
    assert df.count() == 5

    first = df.first().asDict()
    assert first.get('language') == 'JavaScript'
    assert first.get('total_lines') == 93_692
    assert first.get('last_three_years') == 55_253
