# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串 
#  👍 2001 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque

class Solution:
    def __init__(self):
        self.parentheses = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if c not in self.parentheses:
                    return False
                else:
                    if not stack:
                        return False
                    popped = stack.pop()
                    if popped != self.parentheses[c]:
                        return False
        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("{[]}"))
    print(s.isValid("([)]"))
    print(s.isValid("("))
    print(s.isValid("]"))
# leetcode submit region end(Prohibit modification and deletion)
