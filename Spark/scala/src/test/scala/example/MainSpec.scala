package example

import org.apache.spark.sql.functions.col
import org.scalatest.funsuite._

/**
 * Test code for Main.scala.
 *
 * Date: 10/8/2022
 *
 * @author Andrew Jarombek
 */

class MainSpec extends AnyFunSuite {
  test("dataframe count") {
    assert(Main.createDF("../data/exercises.json").count() > 0)
  }

  test("long run data") {
    val df = Main.createDF("../data/exercises.json")
    val long_run_df = Main.longRuns(df)
    assert(long_run_df.count() == 2)

    for (row <- long_run_df.collect()) {
      assert(row.getAs[Double]("miles") >= 10)
    }
  }

  test("order by mileage ascending") {
    val df = Main.createDF("../data/exercises.json")
      .filter(col("type") === "kayak")

    val orderedDf = Main.orderByMileage(df, descending = false)
    assert(orderedDf.count() > 0)

    var prev: Double = 0

    for (row <- orderedDf.collect()) {
      val miles = row.getAs[Double]("miles")
      assert(prev <= miles)
      prev = miles
    }
  }

  test("order by mileage descending") {
    val df = Main.createDF("../data/exercises.json")
      .filter(col("type") === "kayak")

    val orderedDf = Main.orderByMileage(df, descending = true)
    assert(orderedDf.count() > 0)

    var prev = Double.MaxValue

    for (row <- orderedDf.collect()) {
      val miles = row.getAs[Double]("miles")
      assert(prev >= miles)
      prev = miles
    }
  }

  test("walking intensity data") {
    val df = Main.createDF("../data/exercises.json")
    val walkDf = Main.walkIntensity(df)
    assert(walkDf.count() == 5)

    for (row <- walkDf.collect()) {
      val intensity = row.getAs[Long]("intensity")
      assert(intensity >= 1)
    }
  }

  test("grouped exercise mileage") {
    val df = Main.groupedExerciseMileage(Main.createDF("../data/exercises.json"))
    val first = df.first()
    assert(first.getAs[String]("type") == "virtual bike")
  }

  test("create exercise type table") {
    val df = Main.createExerciseTypeTable()
    assert(df.count() == 9)
  }

  test("create languages table") {
    val df = Main.createLanguagesTable()
    assert(df.count() == 5)
  }

  test("sum recent years") {
    val df = Main.sumRecentYears()
    assert(df.count() == 5)

    val first = df.first()
    assert(first.getAs[String]("language") == "JavaScript")
    assert(first.getAs[Int]("total_lines") == 93_692)
    assert(first.getAs[Int]("last_three_years") == 55_253)
  }
}
