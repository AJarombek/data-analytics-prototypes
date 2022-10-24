package example

import org.apache.spark.sql.{DataFrame, Row, SparkSession}
import org.apache.spark.sql.functions._

/**
 * Scala code using Spark.
 *
 * Date: 10/8/2022
 *
 * @author Andrew Jarombek
 */

object Main {
  def createDF(filename: String): DataFrame = {
    val spark = SparkSession
      .builder
      .appName("data-analytics-prototypes")
      .config("spark.master", "local")
      .getOrCreate()

    spark.read
      .option("multiline","true")
      .json(filename)
  }

  def longRuns(data: DataFrame): DataFrame = {
    data
      .where(col("miles") >= 10)
      .where(col("type") === "run")
      .select("date", "location", "miles")
  }

  def main(args: Array[String]): Unit = {
    val filename = args(0)
    val df = createDF(filename)

    println("All Data:")
    df.printSchema()
    df.show()

    println("Long Runs:")
    longRuns(df).show()
  }
}
