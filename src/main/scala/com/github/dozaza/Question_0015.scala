package com.github.dozaza

import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import scala.collection.convert.ImplicitConversionsToScala._

//给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三
//元组。
//
// 注意：答案中不可以包含重复的三元组。
//
//
//
// 示例：
//
// 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
//
//满足要求的三元组集合为：
//[
//  [-1, 0, 1],
//  [-1, -1, 2]
//]
//
// Related Topics 数组 双指针

object Question_0015 {

  def main(args: Array[String]): Unit = {
    val result = threeSum(Array(-1, 0, 1, 2, -1, -4))
    assert(result == List(List(-1, 2, -1), List(0, 1, -1)) ||
      result == List(List(-1, -1, 2), List(-1, 0, 1))
    )
  }

  def threeSum(nums: Array[Int]): List[List[Int]] = {
    if (nums.length < 3) {
      return List.empty
    }

    java.util.Arrays.sort(nums)
    val result = new scala.collection.mutable.ListBuffer[List[Int]]
    var i = 0
    var j = 0
    var k = 0
    while(k < (nums.length - 2) && nums(k) <= 0) {
      if (k > 0 && nums(k - 1) == nums(k)) {
        // skip same number
      } else {
        i = k + 1
        j = nums.length - 1
        while (i < j) {
          val tmp = nums(i) + nums(j) + nums(k)
          if (tmp == 0) {
            result += List(nums(i), nums(j), nums(k))
            i += 1
            j -= 1
            // skip same number
            while (i < j && nums(i) == nums(i - 1)) {
              i += 1
            }
            while (i < j && nums(j) == nums(j + 1)) {
              j -= 1
            }
          } else {
            if (tmp < 0) {
              i += 1
              // skip same number
              while (i < j && nums(i) == nums(i - 1)) {
                i += 1
              }
            } else {
              j -= 1
              // skip same number
              while (i < j && nums(j) == nums(j + 1)) {
                j -= 1
              }
            }
          }
        }
      }
      k += 1
    }

    result.toList
  }

}
