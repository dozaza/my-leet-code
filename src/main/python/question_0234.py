# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针 
#  👍 757 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    # find mid, and reverse rest, and 2 pointers iterate
    # 1->4->3->2->1 => 1->4->3->1->2
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        mid = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            mid = mid.next
            fast = fast.next.next

        mid = self.reverseList(mid.next)
        while mid is not None:
            if mid.val != head.val:
                return False
            mid = mid.next
            head = head.next

        return True

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        new_head = head
        while head.next is not None:
            tmp = new_head
            new_head = head.next
            head.next = new_head.next
            new_head.next = tmp

        return new_head

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(s.isPalindrome(l))
    l2 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
    print(s.isPalindrome(l2))
    l3 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
    print(s.isPalindrome(l3))
    l4 = ListNode(1, ListNode(4, ListNode(2, ListNode(1))))
    print(s.isPalindrome(l4))


# leetcode submit region end(Prohibit modification and deletion)
