package com.github.dozaza;

//给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
//
// 示例 1:
//
// 输入: 123
//输出: 321
//
//
// 示例 2:
//
// 输入: -123
//输出: -321
//
//
// 示例 3:
//
// 输入: 120
//输出: 21
//
//
// 注意:
//
// 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31, 2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
//

public class Question_0007 {

    public static void main(String[] args) {
        int x = -129;
        int res = reverse(x);
        System.out.println(res);
    }

    public static int reverse(int x) {
        boolean isNegative = x < 0;
        long absX = isNegative ? -1 * x : x;

        // int: -2147483648 ~ 2147483647

        int[] nums = new int[10];

        int length = 0;

        for (int i = 9; i >=0; i--) {
            int h = (int) Math.pow(10, i);
            int r = (int) absX / h;
            if (length == 0 && r != 0) {
                length = i;
            }

            nums[i] = r;
            absX -= r * h;
        }

        long reversed = 0L;
        for (int i = 0; i <= length; i++) {
            if (nums[i] > 0) {
                reversed += nums[i] * Math.pow(10, (length - i));
            }
        }

        if (isNegative) {
            reversed *= -1;
        }

        if (reversed < Integer.MIN_VALUE || reversed > Integer.MAX_VALUE) {
            return 0;
        } else {
            return (int) reversed;
        }
    }




}
