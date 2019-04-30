package com.github.dozaza;

//给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
//
// 示例 1:
//
// 输入: "abcabcbb"
//输出: 3
//解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
//
//
// 示例 2:
//
// 输入: "bbbbb"
//输出: 1
//解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
//
//
// 示例 3:
//
// 输入: "pwwkew"
//输出: 3
//解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
//     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
//
//

import java.util.HashMap;
import java.util.Map;

public class Question_0003 {

    public static void main(String[] args) {
        String s = "pwwkew";
        int res = lengthOfLongestSubstring(s);
        System.out.println(res);
    }

    public static int lengthOfLongestSubstring(String s) {
        char[] array = s.toCharArray();

        Map<Character, Integer> charMap = new HashMap<>();
        int start = 0;
        int max = 0;
        for (int i = 0; i < array.length; i++) {
            Character c = array[i];
            if (charMap.containsKey(c)) {
                int duplicateIdx = charMap.get(c);
                for (int j = start; j <= duplicateIdx; j++) {
                    charMap.remove(array[j]);
                }
                start = duplicateIdx + 1;
            }
            charMap.put(c, i);
            if (charMap.size() > max) {
                max = charMap.size();
            }
        }

        return max;
    }

}
