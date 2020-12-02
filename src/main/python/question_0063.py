# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
# 
#  示例 2： 
# 
#  
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] 为 0 或 1 
#  
#  Related Topics 数组 动态规划 
#  👍 450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    # dp[i,j] = 0 if o[i][j] == 1 else dp[i-1][j] + dp[i][j-1]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = []
        for j in range(n):
            dp.append([0] * m)

        dp[0][0] = 1
        for i in range(1, n):
            if dp[i-1][0] > 0 and obstacleGrid[i][0] != 1:
                dp[i][0] = 1
        for j in range(1, m):
            if dp[0][j-1] > 0 and obstacleGrid[0][j] != 1:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
# leetcode submit region end(Prohibit modification and deletion)
