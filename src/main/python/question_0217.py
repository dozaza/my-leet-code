# 给定一个整数数组，判断是否存在重复元素。 
# 
#  如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,3,1]
# 输出: true 
# 
#  示例 2: 
# 
#  输入: [1,2,3,4]
# 输出: false 
# 
#  示例 3: 
# 
#  输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true 
#  Related Topics 数组 哈希表 
#  👍 289 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in range(0, len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

# leetcode submit region end(Prohibit modification and deletion)
