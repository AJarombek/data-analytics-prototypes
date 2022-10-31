"""
Python code using Spark.
Author: Andrew Jarombek
Date: 10/9/2022
"""

import sys

from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F


def create_df(filename: str) -> DataFrame:
    """
    Create a Spark dataframe using a local spark session.
    :param filename: Name of a JSON file to read into a dataframe.
    :return: A pyspark dataframe reflecting the data in a JSON file.
    """
    spark = (
        SparkSession.builder.appName('data-analytics-prototypes')
        .config("spark.master", "local")
        .getOrCreate()
    )

    return spark.read.option("multiline", "true").json(filename)


def long_runs(data: DataFrame) -> DataFrame:
    """
    Filter a dataframe containing exercise information to include only long runs.
    :param data: A dataframe containing exercise data.
    :return: Long run data in a dataframe.
    """
    return (
        data.where(F.col("miles") >= 10)
        .where(F.col("type") == "run")
        .select("date", "location", "miles")
    )


def order_by_mileage(data: DataFrame, desc: bool = True) -> DataFrame:
    """
    Order a dataframe of exercises by their mileage.
    :param data: A dataframe containing exercise data.
    :param desc: Whether the exercises should be ordered in descending order or not.
    :return: Ordered data in a dataframe.
    """
    return data.orderBy(F.desc("miles") if desc else F.col("miles"))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No JSON File Specified")
        exit(1)

    df = create_df(sys.argv[1])
    print(df.schema)

    print("All Data:")
    print(df.show())

    long_run_df = long_runs(df)
    print("Long Runs:")
    print(long_run_df.show())

    print("Ordered Long Runs:")
    print(order_by_mileage(long_run_df).show())
