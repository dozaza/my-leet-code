package com.github.dozaza

object main {

  def main(args: Array[String]): Unit = {
    println({
      val q1 = Question1.twoSum(Array(2, 7, 11, 15), 9)
      q1(0) + ", " + q1(1)
    })
  }

  object Question1 {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
      if (nums.isEmpty) {
        return Array.empty
      }

      nums.zipWithIndex.par.foreach{ case(num, i) =>
        (i + 1 until nums.length).foreach { j =>
          if (nums(j) + num == target) {
            return Array(i, j)
          }
        }
      }

      Array.empty
    }

    def twoSumUpdate(nums: Array[Int], target: Int): Array[Int] = {
      if (nums.isEmpty) {
        return Array.empty
      }

      val numMap = nums.zipWithIndex.toMap
      val diff = nums.zipWithIndex.map{ case(n, i) => (target - n, i) }

      diff.foreach{ case(d, i) =>
        if (numMap.contains(d) && i != numMap(d)) {
          return Array(i, numMap(d))
        }
      }

      Array.empty
    }
  }

}


