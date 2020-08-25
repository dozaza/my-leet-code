# 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。 
# 
#  返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有： 
# 
#  
#  如果 S[i] == "I"，那么 A[i] < A[i+1] 
#  如果 S[i] == "D"，那么 A[i] > A[i+1] 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入："IDID"
# 输出：[0,4,1,3,2]
#  
# 
#  示例 2： 
# 
#  输入："III"
# 输出：[0,1,2,3]
#  
# 
#  示例 3： 
# 
#  输入："DDI"
# 输出：[3,2,0,1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= S.length <= 10000 
#  S 只包含字符 "I" 或 "D"。 
#  
#  Related Topics 数学 
#  👍 162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        n = len(S)
        if n == 0:
            return []
        nums = list(range(0, n + 1))
        result = [0] * (n + 1)
        for i in range(0, n):
            c = S[i]
            if c == 'I':
                result[i] = nums.pop(0)
            else:
                result[i] = nums.pop(-1)
        result[-1] = nums[-1]
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.diStringMatch("IDID"))
    print(s.diStringMatch("III"))
    print(s.diStringMatch("DDI"))
# leetcode submit region end(Prohibit modification and deletion)
