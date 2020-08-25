# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 8974 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import defaultdict

class Solution:

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # Optimization: save diff into map when iterating
        if len(nums) <= 1:
            return []

        diff_idx_map = {}
        for i in range(0, len(nums)):
            n = nums[i]
            diff = target - n
            if diff in diff_idx_map:
                return [i, diff_idx_map[diff]]
            diff_idx_map[n] = i

        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            return []

        num_cnt_map = defaultdict(list)
        for i in range(0, len(nums)):
            num_cnt_map[nums[i]].append(i)

        for i in range(0, len(nums)):
            n = nums[i]
            diff = target - n
            diff_indices = num_cnt_map[diff]
            if len(diff_indices) > 0:
                if diff != n:
                    return [i, diff_indices[0]]
                elif len(diff_indices) > 1:
                    return diff_indices[:2]

        return []

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum2([2, 11, 7, 11, 11, 15], 26))
    print(s.twoSum2([2, 11, 7, 11, 11, 15], 22))
    print(s.twoSum2([2, 11, 7], 22))
# leetcode submit region end(Prohibit modification and deletion)
