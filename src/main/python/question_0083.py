# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
# 
#  示例 1: 
# 
#  输入: 1->1->2
# 输出: 1->2
#  
# 
#  示例 2: 
# 
#  输入: 1->1->2->3->3
# 输出: 1->2->3 
#  Related Topics 链表 
#  👍 416 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        cur = head
        while cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

    def printListNode(self, head: ListNode):
        values = []
        while head is not None:
            values.append(str(head.val))
            head = head.next
        print('->'.join(values))

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1, ListNode(1, ListNode(2)))
    l1 = s.deleteDuplicates(l1)
    s.printListNode(l1)

    l2 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = s.deleteDuplicates(l2)
    s.printListNode(l2)


# leetcode submit region end(Prohibit modification and deletion)
