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

  test("create exercise type table") {
    val df = Main.createExerciseTypeTable()
    assert(df.count() == 9)
  }

  test("create languages table") {
    val df = Main.createLanguagesTable()
    assert(df.count() == 5)
  }
}
