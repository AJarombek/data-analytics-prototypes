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
    assert(Main.createDF("exercises.json").count() > 0)
  }
}
