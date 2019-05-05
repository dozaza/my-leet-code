package com.github.dozaza;

//给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
//
// 示例 1：
//
// 输入: "babad"
//输出: "bab"
//注意: "aba" 也是一个有效答案。
//
//
// 示例 2：
//
// 输入: "cbbd"
//输出: "bb"
//
//


public class Question_0005 {

    public static void main(String[] args) {
        String res = longestPalindrome("babad");
        System.out.println(res);
    }

    public static String longestPalindrome(String s) {
        if (s.length() <= 1) {
            return s;
        }
        // dp[i][j] = s[i] == s[j] && d[i+1][j-1], dp[i][j] means substring s[i:j] (contains j) is a palindrome
        int n = s.length();
        char[] sArray = s.toCharArray();
        boolean[][] dp = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        int left = 0, right = 0;
        for (int j = 0; j < n; j++) {
            for (int i = 0; i <= j; i++) {
                dp[i][j] = sArray[i] == sArray[j] && (j - i < 2 || (j > 0 && dp[i+1][j-1]));
                if (dp[i][j] && (j - i) > (right - left)) {
                    right = j;
                    left = i;
                }
            }
        }
        return s.substring(left, right + 1);
    }




}
