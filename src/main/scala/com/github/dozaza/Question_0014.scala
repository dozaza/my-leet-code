package com.github.dozaza

//编写一个函数来查找字符串数组中的最长公共前缀。
//
// 如果不存在公共前缀，返回空字符串 ""。
//
// 示例 1:
//
// 输入: ["flower","flow","flight"]
//输出: "fl"
//
//
// 示例 2:
//
// 输入: ["dog","racecar","car"]
//输出: ""
//解释: 输入不存在公共前缀。
//
//
// 说明:
//
// 所有输入只包含小写字母 a-z 。
// Related Topics 字符串

object Question_0014 {

  def main(args: Array[String]): Unit = {
    assert(longestCommonPrefix(Array("flower","flow","flight")) == "fl")
    assert(longestCommonPrefix(Array("dog","racecar","car")) == "")
  }

  def longestCommonPrefix(strs: Array[String]): String = {
    if (strs.isEmpty) {
      return ""
    }

    if (strs.length == 1) {
      return strs.head
    }

    var isSamePrefix = true
    var i = 0
    val minLength = strs.map(_.length).min
    if (minLength == 0) {
      return ""
    }

    while (isSamePrefix && i < minLength) {
      val first = strs.head(i)
      isSamePrefix = strs.tail.foldLeft((first, true)) { case((first, flag), str) =>
        (first, str(i) == first && flag)
      }._2

      if (isSamePrefix) {
        i += 1
      }
    }

    strs.head.substring(0, i)
  }

}
