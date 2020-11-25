# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。 
# 
#  对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。 
# 
#  你可以返回任何满足上述条件的数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length <= 20000 
#  A.length % 2 == 0 
#  0 <= A[i] <= 1000 
#  
# 
#  
#  Related Topics 排序 数组 
#  👍 182 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even, odd = 0, 1
        size = len(A)
        while even < size and odd < size:
            while even < size and A[even] % 2 == 0:
                even += 2
            while odd < size and A[odd] % 2 == 1:
                odd += 2
            if odd < size and even < size:
                A[even], A[odd] = A[odd], A[even]
            even += 2
            odd += 2
        return A

if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParityII([7,2,5,4]))
    print(s.sortArrayByParityII([7,2,5,4,6,5]))
    print(s.sortArrayByParityII([2,3]))
    print(s.sortArrayByParityII([3,0,4,0,2,1,3,1,3,4]))

# leetcode submit region end(Prohibit modification and deletion)
