package com.github.dozaza;

//将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
//
// 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
//
// L   C   I   R
//E T O E S I I G
//E   D   H   N
//
//
// 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
//
// 请你实现这个将字符串进行指定行数变换的函数：
//
// string convert(string s, int numRows);
//
// 示例 1:
//
// 输入: s = "LEETCODEISHIRING", numRows = 3
//输出: "LCIRETOESIIGEDHN"
//
//
// 示例 2:
//
// 输入: s = "LEETCODEISHIRING", numRows = 4
//输出: "LDREOEIIECIHNTSG"
//解释:
//
//L     D     R
//E   O E   I I
//E C   I H   N
//T     S     G
//

public class Question_0006 {

    public static void main(String[] args) {
        String s = "LEETCODEISHIRING";
        String res = convert(s, 4);
        System.out.println(res);
    }

    public static String convert(String s, int numRows) {
        if (null == s || s.length() <= 1 || numRows <= 1) {
            return s;
        }

        char[] charArray = s.toCharArray();
        StringBuilder sb = new StringBuilder();
        int interval = numRows + numRows - 2;
        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < s.length(); j = j + interval) {
                sb.append(charArray[j]);
                if (0 < i && i < numRows - 1) {
                    int mid = j + 2 * (numRows - i - 1);
                    if (mid >= s.length()) {
                        break;
                    }

                    sb.append(charArray[mid]);
                }
            }
        }

        return sb.toString();
    }




}
