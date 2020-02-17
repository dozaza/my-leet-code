package com.github.dozaza

//给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
//ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
//
// 说明：你不能倾斜容器，且 n 的值至少为 2。
//
//
//)"
// 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
//
//
//
// 示例:
//
// 输入: [1,8,6,2,5,4,8,3,7]
//输出: 49
// Related Topics 数组 双指针


object Question_0011 {

  def main(args: Array[String]): Unit = {
    assert(maxArea(Array(1,8,6,2,5,4,8,3,7)) == 49)
  }

  def maxArea(height: Array[Int]): Int = {
    if (height.isEmpty || height.length <= 1) {
      return -1
    }

    var i = 0
    var j = height.length - 1
    var res = 0

    // 头尾 2 个指针同时移动，若要发现一个更大面积，只能是较小的那根朝内移动。
    while(i < j) {
      val h = math.min(height(i), height(j))
      res = math.max(res, h * (j - i))
      if (height(i) < height(j)) {
        i += 1
      } else {
        j -= 1
      }
    }

    res
  }

}
