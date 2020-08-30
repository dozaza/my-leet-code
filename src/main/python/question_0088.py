# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针 
#  👍 599 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Optimization by iterating from end
        if n == 0:
            return

        if m == 0:
            nums1[:n] = nums2
            return

        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        if j >= 0:
            nums1[0:j+1] = nums2[0:j+1]


    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            nums1[:n] = nums2
            return

        res = [0] * (m + n)
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res[i + j] = nums1[i]
                i += 1
            else:
                res[i + j] = nums2[j]
                j += 1

        if i < m:
            res[i+j:] = nums1[i:m]
        if j < n:
            res[i+j:] = nums2[j:n]

        nums1[:] = res


if __name__ == '__main__':
    s = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge2(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0,0,0]
    m = 0
    nums2 = [2,5,6]
    n = 3
    s.merge2(nums1, m, nums2, n)
    print(nums1)

    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge2(nums1, m, nums2, n)
    print(nums1)

# leetcode submit region end(Prohibit modification and deletion)
