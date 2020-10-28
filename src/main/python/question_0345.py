# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入："hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  输入："leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  元音字母不包含字母 "y" 。 
#  
#  Related Topics 双指针 字符串 
#  👍 121 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def reverseVowels(self, s: str) -> str:
        if len(s) <= 0:
            return s

        i, j = 0, len(s) - 1
        a = [c for c in s]
        while i < j:
            while i < j and a[i] not in self.vowels:
                i += 1
            while i < j and a[j] not in self.vowels:
                j -= 1
            if i >= j:
                break
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        return ''.join(a)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels('leetcode'))

# leetcode submit region end(Prohibit modification and deletion)
