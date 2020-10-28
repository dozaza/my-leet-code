# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表 
#  👍 1345 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        c = ListNode()
        l = c
        while l1 is not None and l2 is not None:
            val = l1.val if l1.val < l2.val else l2.val
            c.next = ListNode(val)
            c = c.next
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next

        if l1 is not None:
            c.next = l1
        else:
            c.next = l2

        return l.next

    def mkString(self, l: ListNode) -> str:
        values = []
        while l is not None:
            values.append(str(l.val))
            l = l.next
        return '->'.join(values)


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(1, ListNode(5))
    print(s.mkString(s.mergeTwoLists(l1, l2)))
    print(s.mkString(s.mergeTwoLists(l1, l3)))

# leetcode submit region end(Prohibit modification and deletion)
