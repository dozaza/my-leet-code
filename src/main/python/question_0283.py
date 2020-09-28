# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。 
# 
#  示例: 
# 
#  输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0] 
# 
#  说明: 
# 
#  
#  必须在原数组上操作，不能拷贝额外的数组。 
#  尽量减少操作次数。 
#  
#  Related Topics 数组 双指针 
#  👍 719 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # j: idx of 0, i: idx of none-0
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
    print(nums)


# leetcode submit region end(Prohibit modification and deletion)
