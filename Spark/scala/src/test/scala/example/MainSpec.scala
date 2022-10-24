package example

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
}
