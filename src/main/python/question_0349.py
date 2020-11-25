# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
#  
# 
#  示例 2： 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中的每个元素一定是唯一的。 
#  我们可以不考虑输出结果的顺序。 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    # return list(set(nums1) & set(nums2))
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None:
            nums1 = []
        if nums2 is None:
            nums2 = []
        nums1 = set(nums1)
        result = set()
        for num in nums2:
            if num in nums1:
                result.add(num)
        return list(result)


if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5], [9,4,9,8,4]))
    print(s.intersection([], [9,4,9,8,4]))

# leetcode submit region end(Prohibit modification and deletion)
