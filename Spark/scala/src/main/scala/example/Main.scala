package example

import example.Main.sparkSession
import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.{IntegerType, StringType, StructField, StructType}

/**
 * Scala code using Spark.
 *
 * Date: 10/8/2022
 *
 * @author Andrew Jarombek
 */

object Main {
  /**
   * Get or create a spark session.
   * @return A spark session object.
   */
  def sparkSession(): SparkSession = {
    SparkSession
      .builder
      .appName("data-analytics-prototypes")
      .config("spark.master", "local")
      .getOrCreate()
  }

  /**
   * Create a Spark dataframe using a local spark session.
   * @param filename Name of a JSON file to read into a dataframe.
   * @return A pyspark dataframe reflecting the data in a JSON file.
   */
  def createDF(filename: String): DataFrame = {
    sparkSession().read
      .option("multiline","true")
      .json(filename)
  }

  /**
   * Filter a dataframe containing exercise information to include only long runs.
   * @param data A dataframe containing exercise data.
   * @return Long run data in a dataframe.
   */
  def longRuns(data: DataFrame): DataFrame = {
    data
      .where(col("miles") >= 10)
      .where(col("type") === "run")
      .select("date", "location", "miles")
  }

  /**
   * Order a dataframe of exercises by their mileage.
   * @param data A dataframe containing exercise data.
   * @param descending Whether the exercises should be ordered in descending order or not.
   * @return Ordered exercise data in a dataframe.
   */
  def orderByMileage(data: DataFrame, descending: Boolean): DataFrame = {
    data.orderBy(if (descending) desc("miles") else col("miles"))
  }

  /**
   * Create a dataframe containing walking exercises that are over an hour.
   *  Uses withColumnRenamed() to rename a column.
   * @param data A dataframe containing exercise data.
   * @return Long walk exercises in a dataframe.
   */
  def walkIntensity(data: DataFrame): DataFrame = {
    val ss = sparkSession()
    import ss.implicits._

    data
      .withColumnRenamed("hours", "intensity")
      .where($"type" === "walk")
      .select("date", "location", "intensity")
      .where($"intensity" > 0)
  }

  /**
   * Create a dataframe containing exercise types.  The dataframe is created using a data set
   * and a programmatically created schema.
   * @return A dataframe containing exercise types.
   */
  def createExerciseTypeTable(): DataFrame = {
    val schema = StructType(Array(
      StructField("id", IntegerType, nullable = false),
      StructField("type", StringType, nullable = false)
    ))

    val data = Seq(
      Row(1, "run"),
      Row(2, "bike"),
      Row(3, "kayak"),
      Row(4, "core"),
      Row(5, "strength"),
      Row(6, "downhill ski"),
      Row(7, "nordic ski"),
      Row(8, "yoga"),
      Row(9, "swim"),
    )

    val spark = sparkSession()
    spark.createDataFrame(spark.sparkContext.parallelize(data), schema)
  }

  /**
   * Create a dataframe containing programming language information & statistics.  The dataframe is
   *  created using a data set and a string schema.
   * @return A dataframe containing programming language statistics.
   */
  def createLanguagesTable(): DataFrame = {
    val schema = "language STRING, first_year_coded INT, total_lines INT, lines ARRAY<INT>"
    val data = Seq(
      Row("JavaScript", 2016, 93_692, Seq(42_578, 10_176, 2_499)),
      Row("Python", 2015, 78_580, Seq(16_740, 19_917, 16_415)),
      Row("Java", 2014, 50_122, Seq(2_042, 5_206, 2_724)),
      Row("TypeScript", 2017, 44_290, Seq(11_830, 23_555, 6_036)),
      Row("HTML", 2016, 50_122, Seq(2_484, 4_988, 2_571)),
    )

    val spark = sparkSession()
    spark.createDataFrame(spark.sparkContext.parallelize(data), StructType.fromDDL(schema))
  }

  def main(args: Array[String]): Unit = {
    val filename = args(0)
    val df = createDF(filename)

    println("All Data:")
    df.printSchema()
    df.show()

    println("Long Runs:")
    val longRunDf = longRuns(df)
    longRunDf.show()

    println("Ordered Long Runs:")
    orderByMileage(longRunDf, descending = true).show()

    println("Long Walk Intensity:")
    walkIntensity(df).show()
  }
}
