# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。 
# 
#  说明：本题中，我们将空字符串定义为有效的回文串。 
# 
#  示例 1: 
# 
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "race a car"
# 输出: false
#  
#  Related Topics 双指针 字符串 
#  👍 285 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def is_char(self, c: str):
        return ('a' <= c and c <= 'z') or ('0' <= c and c <= '9')

    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.is_char(s[i]):
                i += 1
            while i < j and not self.is_char(s[j]):
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome('A man, a plan, a canal: Panama'))
    print(s.isPalindrome('race a car'))
    print(s.isPalindrome('.,'))
# leetcode submit region end(Prohibit modification and deletion)
