# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。 
# 
#  每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。 
# 
#  您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。 
# 
#  示例 1: 
# 
#  输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
#  
# 
#  示例 2: 
# 
#  输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
#  
# 
#  注意： 
# 
#  
#  cost 的长度将会在 [2, 1000]。 
#  每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。 
#  
#  Related Topics 数组 动态规划 
#  👍 357 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        # Optimization for dp[i] = min(dp[i-1] + dp[i-2]) + cost[i]
        size = len(cost)
        if size == 0:
            return 0
        if size == 1:
            return cost[0]

        # i-2, i-1
        prev, curr = cost[0], cost[1]
        for i in range(2, size + 1):
            c = cost[i] if i < size else 0
            if prev + c > curr + c:
                prev, curr = curr, curr + c
            else:
                prev, curr = curr, prev + c
        return min(prev, curr)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Question explanation: when you climb to the step, your cost should increase corresponding delta.
        # dp[i] = min(dp[i-1] + dp[i-2]) + cost[i]
        size = len(cost)
        if size == 0:
            return 0
        if size == 1:
            return cost[0]

        dp = [0] * (size + 1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, size + 1):
            c = cost[i] if i < size else 0
            dp[i] = min(dp[i-1], dp[i-2]) + c

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(s.minCostClimbingStairs2([10, 15, 20]))
# leetcode submit region end(Prohibit modification and deletion)
