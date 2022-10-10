"""
Python code using Spark.
Author: Andrew Jarombek
Date: 10/9/2022
"""

import sys

from pyspark.sql import SparkSession, DataFrame


def create_df(filename: str) -> DataFrame:
    spark = (
        SparkSession.builder.appName('data-analytics-prototypes')
        .config("spark.master", "local")
        .getOrCreate()
    )

    return spark.read.option("multiline", "true").json(filename)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("No JSON File Specified")
        exit(1)

    df = create_df(sys.argv[1])
    print(df.schema)
    print(df.show())
