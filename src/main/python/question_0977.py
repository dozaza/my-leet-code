# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#  
# 
#  示例 2： 
# 
#  输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A 已按非递减顺序排序。 
#  
#  Related Topics 数组 双指针 
#  👍 170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        # two pointer, one from left, one from right
        res = [0] * len(A)
        i, j, k = 0, len(A) - 1, len(res) - 1
        while i <= j:
            num1 = A[i] * A[i]
            num2 = A[j] * A[j]
            if num1 > num2:
                res[k] = num1
                i += 1
            else:
                res[k] = num2
                j -= 1
            k -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-7,-3,2,3,11]))
    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-4,-1,0,3]))
# leetcode submit region end(Prohibit modification and deletion)
