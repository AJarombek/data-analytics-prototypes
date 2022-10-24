"""
Test code for python programs using Spark.
Author: Andrew Jarombek
Date: 10/10/2022
"""

import os

import pytest

from da_spark_prototypes.main import create_df, long_runs


@pytest.fixture()
def data():
    filename = os.path.join(
        os.path.dirname(__file__), "../../..", "data/exercises.json"
    )
    return create_df(filename)


def test_create_df(data):
    assert data.count() > 0


def test_long_runs(data):
    long_run_data = long_runs(data)
    assert long_run_data.count() == 2

    for row in long_run_data.collect():
        data = row.asDict()
        assert data.get('miles') >= 10
