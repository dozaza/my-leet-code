package com.github.dozaza;

//判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
//
// 示例 1:
//
// 输入: 121
//输出: true
//
//
// 示例 2:
//
// 输入: -121
//输出: false
//解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
//
//
// 示例 3:
//
// 输入: 10
//输出: false
//解释: 从右向左读, 为 01 。因此它不是一个回文数。
//
//
// 进阶:
//
// 你能不将整数转为字符串来解决这个问题吗？
//


public class Question_0009 {

    public static void main(String[] args) {
        int x = 121;
        boolean res = isPalindrome(x);
        System.out.println(res);
    }

    public static boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int length = 0;
        int temp = x;
        while (temp != 0) {
            temp /= 10;
            length++;
        }

        int left = length - 1;
        int right = 0;

        while (left > right) {
            if (getDigit(x, left--) != getDigit(x, right++))
                return false;
        }

        return true;
    }

    private static int getDigit(int x, int i) {
        x = x / (int) Math.pow(10, i);
        return x % 10;
    }
}
