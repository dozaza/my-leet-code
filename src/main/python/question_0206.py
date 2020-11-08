# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL 
# 
#  进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？ 
#  Related Topics 链表 
#  👍 1326 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
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

    def printListNode(self, head: ListNode):
        values = []
        while head is not None:
            values.append(str(head.val))
            head = head.next
        print('->'.join(values))

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    l = s.reverseList(l)
    s.printListNode(l)
    l = ListNode(1, ListNode(2))
    l = s.reverseList(l)
    s.printListNode(l)

# leetcode submit region end(Prohibit modification and deletion)
