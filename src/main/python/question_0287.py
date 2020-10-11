# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出
# 这个重复的数。
#
#  示例 1:
#
#  输入: [1,3,4,2,2]
# 输出: 2
#
#
#  示例 2:
#
#  输入: [3,1,3,4,2]
# 输出: 3
#
#
#  说明：
#
#
#  不能更改原数组（假设数组是只读的）。
#  只能使用额外的 O(1) 的空间。
#  时间复杂度小于 O(n2) 。
#  数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#  Related Topics 数组 双指针 二分查找
#  👍 884 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    # 二分查找，不断遍历 nums 找 mid
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low < high:
            mid = low + int((high - low) / 2)
            cnt = sum([num <= mid for num in nums])
            if cnt > mid:
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))
    print(s.findDuplicate([3,1,3,4,2]))

# leetcode submit region end(Prohibit modification and deletion)
