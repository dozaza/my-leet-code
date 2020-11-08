# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5
#  
#  Related Topics 链表 
#  👍 475 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        new_head = ListNode(-1, head)
        prev = new_head
        curr = head
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return new_head.next

    def printListNode(self, head: ListNode):
        values = []
        while head is not None:
            values.append(str(head.val))
            head = head.next
        print('->'.join(values))

if __name__ == '__main__':
    s = Solution()
    h = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    h = s.removeElements(h, 6)
    s.printListNode(h)
    h = ListNode(1, ListNode(1))
    h = s.removeElements(h, 1)
    s.printListNode(h)


# leetcode submit region end(Prohibit modification and deletion)
