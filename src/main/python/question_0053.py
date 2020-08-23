# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  示例:
#
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
#  进阶:
#
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治算法 动态规划
#  👍 2320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] is the sum of sub seq
        # if sub seq is negative, then max sum sub seq is in the following part
        # if dp[i-1] <= 0:
        #   dp[i] = nums[i]
        # else:
        #   dp[i] = nums[i] + dp[i-1]
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] <= 0:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i-1]
            res = max(res, dp[i])
        return res
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    Solution().maxSubArray([])
