# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上
# 被小偷闯入，系统会自动报警。 
# 
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。 
# 
#  示例 2： 
# 
#  输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics 动态规划 
#  👍 1031 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def rob2(self, nums: List[int]) -> int:
        # optimization for dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        prev_res = nums[0]
        res = max(nums[0], nums[1])
        for i in range(2, size):
            tmp = res
            res = max(res, nums[i] + prev_res)
            prev_res = tmp
        return res

    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # no need to consider dp[i-3] cause if dp[i-3] is larger then dp[i-2], then dp[i-1] is the largest.
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

if __name__ == '__main__':
    nums = [9,2,3,7,1]
    print(Solution().rob2(nums))
# leetcode submit region end(Prohibit modification and deletion)
