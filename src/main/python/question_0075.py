# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。 
# 
#  此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。 
# 
#  
# 
#  进阶： 
# 
#  
#  你可以不使用代码库中的排序函数来解决这道题吗？ 
#  你能想出一个仅使用常数空间的一趟扫描算法吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[0]
#  
# 
#  示例 4： 
# 
#  
# 输入：nums = [1]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  nums[i] 为 0、1 或 2 
#  
#  Related Topics 排序 数组 双指针 
#  👍 708 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:

    def sortColors(self, nums: List[int]) -> None:
        zero_idx = 0
        one_idx = 0
        two_idx = 0
        for num in nums:
            if num == 0:
                nums[two_idx] = 2
                two_idx += 1
                nums[one_idx] = 1
                one_idx += 1
                nums[zero_idx] = 0
                zero_idx += 1
            elif num == 1:
                nums[two_idx] = 2
                two_idx += 1
                nums[one_idx] = 1
                one_idx += 1
            else:
                nums[two_idx] = 2
                two_idx += 1

    def sortColors1(self, nums: List[int]) -> None:
        zero_size = 0
        one_size = 0
        for num in nums:
            if num == 0:
                zero_size += 1
            elif num == 1:
                one_size += 1

        nums[0:zero_size] = [0] * zero_size
        nums[zero_size:(zero_size+one_size)] = [1] * one_size
        nums[(zero_size+one_size):] = [2] * (len(nums) - zero_size - one_size)


    # This method uses O(n) space
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        ones = []
        twos = []
        for num in nums:
            if num == 0:
                zeros.append(num)
            elif num == 1:
                ones.append(num)
            else:
                twos.append(num)

        max_zero_idx = len(zeros)
        max_one_idx = len(ones) + max_zero_idx

        for i in range(0, len(nums)):
            if i < max_zero_idx:
                nums[i] = zeros[i]
            elif i < max_one_idx:
                nums[i] = ones[i - max_zero_idx]
            else:
                nums[i] = twos[i - max_one_idx]

if __name__ == '__main__':
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    print(nums)

# leetcode submit region end(Prohibit modification and deletion)
