package example

import org.apache.spark.sql.{DataFrame, Row, SparkSession}

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
      .format("json")
      .option("inferSchema", "true")
      .load(filename)
  }

  def main(args: Array[String]): Unit = {
    val filename = args(0)
    val df = createDF(filename)
    df.show()
  }
}
