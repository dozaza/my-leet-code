# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。 
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3]
# 输出: 6
#  
# 
#  示例 2: 
# 
#  
# 输入: [1,2,3,4]
# 输出: 24
#  
# 
#  注意: 
# 
#  
#  给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。 
#  输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。 
#  
#  Related Topics 数组 数学 
#  👍 181 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top1, top2, top3 = -1001, -1001, -1001
        bot1, bot2 = 0, 0
        for i in range(len(nums)):
            num = nums[i]
            if num > top1:
                top1, top2, top3 = num, top1, top2
            elif num > top2:
                top2, top3 = num, top2
            elif num > top3:
                top3 = num
            if num < bot1:
                bot1, bot2 = num, bot1
            elif num < bot2:
                bot2 = num

        max = top1 * top2 * top3
        min_neg = bot1 * bot2
        if min_neg > 0:
            max2 = min_neg * top1
            if max2 > max:
                max = max2

        return max

if __name__ == '__main__':
    s = Solution()
    print(s.maximumProduct([1,2,3,4]))
    print(s.maximumProduct([-1,-2,-4,-3,-6,-5]))
    print(s.maximumProduct([-4,-3,-2,-1,60]))

# leetcode submit region end(Prohibit modification and deletion)
