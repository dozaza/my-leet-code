# 给定一个矩阵 A， 返回 A 的转置矩阵。 
# 
#  矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#  
# 
#  示例 2： 
# 
#  输入：[[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 1000 
#  1 <= A[0].length <= 1000 
#  
#  Related Topics 数组 
#  👍 115 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(A[0]) == 0:
            return A

        r = len(A)
        c = len(A[0])

        A_t = [[0] * r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                A_t[j][i] = A[i][j]

        return A_t
# leetcode submit region end(Prohibit modification and deletion)
