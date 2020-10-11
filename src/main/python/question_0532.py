# 给定一个整数数组和一个整数 k，你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j)，其中 i 和 j 都
# 是数组中的数字，且两数之差的绝对值是 k 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[3, 1, 4, 1, 5], k = 2
# 输出：2
# 解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
#  
# 
#  示例 2： 
# 
#  输入：[1, 2, 3, 4, 5], k = 1
# 输出：4
# 解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
#  
# 
#  示例 3： 
# 
#  输入：[1, 3, 1, 5, 4], k = 0
# 输出：1
# 解释：数组中只有一个 0-diff 数对，(1, 1)。
#  
# 
#  示例 4： 
# 
#  输入：nums = [1,2,4,4,3,3,0,9,2,3], k = 3
# 输出：2
#  
# 
#  示例 5： 
# 
#  输入：nums = [-1,-2,-3], k = 1
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 104 
#  -107 <= nums[i] <= 107 
#  0 <= k <= 107 
#  
#  Related Topics 数组 双指针 
#  👍 97 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    # 由于是查找 diff pairs，即就算多组同值 pair，也只算1个，所以可以遍历 map 的 keys，
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1 or k < 0:
            return 0

        cnt_map = {}
        for num in nums:
            if num not in cnt_map:
                cnt_map[num] = 0
            cnt_map[num] = cnt_map[num] + 1

        pair_cnt = 0
        for num in cnt_map.keys():
            if k == 0 and cnt_map[num] > 1:
                pair_cnt += 1
            elif k > 0 and num + k in cnt_map:
                pair_cnt += 1

        return pair_cnt

if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([1, 3, 1, 5, 4], k=0))
    print(s.findPairs([1,2,4,4,3,3,0,9,2,3], k=3))

# leetcode submit region end(Prohibit modification and deletion)
