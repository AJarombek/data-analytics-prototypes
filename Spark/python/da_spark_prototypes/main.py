"""
Python code using Spark.
Author: Andrew Jarombek
Date: 10/9/2022
"""

import sys

from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as F
import pyspark.sql.types as T

from da_spark_prototypes.exercise_table import Exercise


def spark_session() -> SparkSession:
    """
    Get or create a spark session.
    :return: A spark session object.
    """
    return (
        SparkSession.builder.appName('data-analytics-prototypes')
        .config("spark.master", "local")
        .getOrCreate()
    )


def create_df(filename: str) -> DataFrame:
    """
    Create a Spark dataframe using a local spark session.
    :param filename: Name of a JSON file to read into a dataframe.
    :return: A pyspark dataframe reflecting the data in a JSON file.
    """
    spark = spark_session()
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


def walk_intensity(data: DataFrame) -> DataFrame:
    """
    Create a dataframe containing walking exercises that are over an hour.
    Uses withColumnRenamed() to rename a column.
    :param data: A dataframe containing exercise data.
    :return: Long walk exercises in a dataframe
    """
    return (
        data.withColumnRenamed(Exercise.hours, "intensity")
        .where(F.col(Exercise.type) == "walk")
        .select(Exercise.date, Exercise.location, "intensity")
        .where(F.col("intensity") > 0)
    )


def grouped_exercise_mileage(data: DataFrame) -> DataFrame:
    """
    Group exercise data by the exercise type, calculating the total number of miles for each type.
    :param data: A dataframe containing exercise data.
    :return: Grouped mileage data in a dataframe.
    """
    return data.groupBy("type").sum("miles").orderBy(F.desc("sum(miles)"))


def create_exercise_type_table() -> DataFrame:
    """
    Create a dataframe containing exercise types.  The dataframe is created using a data set
    and a programmatically created schema.
    :return: A dataframe containing exercise types.
    """
    spark = spark_session()
    schema = T.StructType(
        [
            T.StructField("id", T.IntegerType(), False),
            T.StructField("type", T.StringType(), False),
        ]
    )

    data = (
        (1, "run"),
        (2, "bike"),
        (3, "kayak"),
        (4, "core"),
        (5, "strength"),
        (6, "downhill ski"),
        (7, "nordic ski"),
        (8, "yoga"),
        (9, "swim"),
    )

    return spark.createDataFrame(data, schema)


def create_languages_table() -> DataFrame:
    """
    Create a dataframe containing programming language information & statistics.  The dataframe is
    created using a data set and a string schema.
    :return:  A dataframe containing programming language statistics.
    """
    spark = spark_session()
    schema = "language STRING, first_year_coded INT, total_lines INT, lines ARRAY<INT>"

    data = [
        ["JavaScript", 2016, 93_692, [42_578, 10_176, 2_499]],
        ["Python", 2015, 78_580, [16_740, 19_917, 16_415]],
        ["Java", 2014, 50_122, [2_042, 5_206, 2_724]],
        ["TypeScript", 2017, 44_290, [11_830, 23_555, 6_036]],
        ["HTML", 2016, 29_469, [2_484, 4_988, 2_571]],
    ]

    return spark.createDataFrame(data, schema)


def sum_recent_years():
    """
    Create a dataframe with programming language data, ordered by the most popular languages in the past three years.
    :return: A dataframe with language data.
    """
    return (
        create_languages_table()
        .withColumn(
            "last_three_years", F.aggregate("lines", F.lit(0), lambda acc, x: acc + x)
        )
        .select("language", "total_lines", "last_three_years")
        .orderBy(F.desc("last_three_years"))
    )


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

    print("Long Walk Intensity:")
    print(walk_intensity(df).show())

    print("Grouped Exercise Miles:")
    print(grouped_exercise_mileage(df).show())

    print("Exercise Types:")
    print(create_exercise_type_table().show())

    print("Programming Languages:")
    print(create_languages_table().show())

    print("Programming Recent Years:")
    print(sum_recent_years().show())
