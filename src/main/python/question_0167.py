# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。 
# 
#  函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。 
# 
#  说明: 
# 
#  
#  返回的下标值（index1 和 index2）不是从零开始的。 
#  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。 
#  
# 
#  示例: 
# 
#  输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。 
#  Related Topics 数组 双指针 二分查找 
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) <= 1:
            return []

        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target:
                i = i + 1
            else:
                j = j - 1

        return []

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))


# leetcode submit region end(Prohibit modification and deletion)
