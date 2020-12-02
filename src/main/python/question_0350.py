# 给定两个数组，编写一个函数来计算它们的交集。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
#  
# 
#  示例 2: 
# 
#  输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9] 
# 
#  
# 
#  说明： 
# 
#  
#  输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。 
#  我们可以不考虑输出结果的顺序。 
#  
# 
#  进阶： 
# 
#  
#  如果给定的数组已经排好序呢？你将如何优化你的算法？ 
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？ 
#  如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？ 
#  
#  Related Topics 排序 哈希表 双指针 二分查找 
#  👍 420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if nums1 is None:
            nums1 = []
        if nums2 is None:
            nums2 = []
        num1_cnt_map = {}
        for num in nums1:
            num1_cnt_map[num] = num1_cnt_map.get(num, 0) + 1
        res = []
        for num in nums2:
            num1_cnt = num1_cnt_map.get(num, 0)
            if num1_cnt > 0:
                res.append(num)
                num1_cnt_map[num] = num1_cnt - 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))
    print(s.intersect([4,5,9],[9,4,9,8,4]))
    print(s.intersect([],[9,4,9,8,4]))
# leetcode submit region end(Prohibit modification and deletion)