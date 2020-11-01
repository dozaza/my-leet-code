# 编写一个程序，找到两个单链表相交的起始节点。 
# 
#  如下面的两个链表： 
# 
#  
# 
#  在节点 c1 开始相交。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, s
# kipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1
# ,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#  
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
#  1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4
# ]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#  
# 
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而
#  skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#  
# 
#  
# 
#  注意： 
# 
#  
#  如果两个链表没有交点，返回 null. 
#  在返回结果后，两个链表仍须保持原有的结构。 
#  可假定整个链表结构中没有循环。 
#  程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 
#  
#  Related Topics 链表 
#  👍 857 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getLength(self, head: ListNode) -> int:
        i = 0
        while head is not None:
            head = head.next
            i += 1
        return i

    # find length diff and longer list move first
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A = self.getLength(headA)
        len_B = self.getLength(headB)
        diff = len_A - len_B

        if diff < 0:
            for _ in range(diff * -1):
                headB = headB.next
        elif diff > 0:
            for _ in range(diff):
                headA = headA.next

        while headA is not None:
            if headA.val == headB.val:
                return headA
            headA = headA.next
            headB = headB.next

        return None

if __name__ == '__main__':
    s = Solution()
    a = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    b = ListNode(5, ListNode(6, ListNode(7, ListNode(3, ListNode(4)))))
    print(s.getIntersectionNode(a, b).val)
    c = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    d = ListNode(5, ListNode(6, ListNode(7)))
    print(s.getIntersectionNode(c, d))
    e = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    f = ListNode(5, ListNode(6, ListNode(4)))
    print(s.getIntersectionNode(e, f).val)
    g = ListNode(4, ListNode(1, ListNode(8, ListNode(6, ListNode(9)))))
    h = ListNode(5, ListNode(6, ListNode(1, ListNode(8, ListNode(6, ListNode(9))))))
    print(s.getIntersectionNode(g, h).val)

# leetcode submit region end(Prohibit modification and deletion)
