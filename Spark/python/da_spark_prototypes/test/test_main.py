"""
Test code for python programs using Spark.
Author: Andrew Jarombek
Date: 10/10/2022
"""

import os

from da_spark_prototypes.main import create_df


def test_create_df():
    filename = os.path.join(os.path.dirname(__file__), "../../..", "data/exercises.json")
    df = create_df(filename)
    assert df.count() > 0
