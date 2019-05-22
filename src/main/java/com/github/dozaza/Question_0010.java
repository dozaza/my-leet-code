package com.github.dozaza;

//给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
//
// '.' 匹配任意单个字符。
//'*' 匹配零个或多个前面的元素。
//
//
// 匹配应该覆盖整个字符串 (s) ，而不是部分字符串。
//
// 说明:
//
//
// s 可能为空，且只包含从 a-z 的小写字母。
// p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
//
//
// 示例 1:
//
// 输入:
//s = "aa"
//p = "a"
//输出: false
//解释: "a" 无法匹配 "aa" 整个字符串。
//
//
// 示例 2:
//
// 输入:
//s = "aa"
//p = "a*"
//输出: true
//解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
//
//
// 示例 3:
//
// 输入:
//s = "ab"
//p = ".*"
//输出: true
//解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
//
//
// 示例 4:
//
// 输入:
//s = "aab"
//p = "c*a*b"
//输出: true
//解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
//
//
// 示例 5:
//
// 输入:
//s = "mississippi"
//p = "mis*is*p*."
//输出: false
//


public class Question_0010 {

    public static void main(String[] args) {
        String s = "aab";
        String p = "*c";
        boolean res = isMatch(s, p);
        System.out.println(res);
    }

    public static boolean isMatch(String s, String p) {
        /**
         * 1. p[j] == s[i] || p[j] == '.':
         *      dp[i][j] = dp[i-1][j-1]
         * 2. p[j] == '*':
         *  2.1 p[j-1] != s[i]:
         *      dp[i][j] = dp[i][j-2]
         *  2.2 p[i-1] == s[i] or p[i-1] == '.':
         *      dp[i][j] = dp[i-1][j] // 多个a的情况
         *      || dp[i][j-1] // 单个a的情况
         *      || dp[i][j-2] // 没有a的情况
         */
        int sLen = s.length();
        int pLen = p.length();
        char[] sArray = s.toCharArray();
        char[] pArray = p.toCharArray();
        boolean[][] dp = new boolean[sLen+1][pLen+1];

        dp[0][0] = true;
        for (int i = 0; i < pLen; i++) {
            if (pArray[i] == '*' && (i == 0 || dp[0][i - 1])) {
                dp[0][i + 1] = true;
            }
        }

        for (int i = 0; i < sLen; i++) {
            for (int j = 0; j < pLen; j++) {
                if (pArray[j] == sArray[i] || pArray[j] == '.') {
                    dp[i + 1][j + 1] = dp[i][j];
                } else if (pArray[j] == '*'){
                    if (j == 0) {
                        dp[i][j] = true;
                    } else {
                        if (pArray[j - 1] != sArray[i]) {
                            dp[i + 1][j + 1] = dp[i + 1][j - 1];
                        } else if (pArray[i - 1] == sArray[i] || pArray[j] == '.') {
                            dp[i + 1][j + 1] = dp[i][j+1] || dp[i + 1][j] || dp[i + 1][j - 1];
                        }
                    }
                }
            }
        }

        return dp[sLen][pLen];
    }

}
