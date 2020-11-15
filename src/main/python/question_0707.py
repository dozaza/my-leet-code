# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针
# /引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。 
# 
#  在链表类中实现这些功能： 
# 
#  
#  get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。 
#  addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。 
#  addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。 
#  addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val 的节点。如果 index 等于链表的长度，则该节点将附加
# 到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。 
#  deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。 
#  
# 
#  
# 
#  示例： 
# 
#  MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
#  
# 
#  
# 
#  提示： 
# 
#  
#  所有val值都在 [1, 1000] 之内。 
#  操作次数将在 [1, 1000] 之内。 
#  请不要使用内置的 LinkedList 库。 
#  
#  Related Topics 设计 链表 
#  👍 184 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: ListNode = None
        self.size = 0

    def __getNode(self, index: int) -> ListNode:
        valid_idx = index if index >= 0 else (self.size + index)

        if self.size <= valid_idx:
            return None

        if valid_idx > self.size / 2:
            r = range(valid_idx + 1, self.size)
            forward = False
            p = self.head.prev
        else:
            r = range(0, valid_idx)
            forward = True
            p = self.head
        for _ in r:
            if forward:
                p = p.next
            else:
                p = p.prev
        return p

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.__getNode(index)
        if node is None:
            return -1

        return node.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.head.prev = self.head
            self.head.next = self.head
            self.size += 1
        else:
            tail = self.head.prev
            node.prev = tail
            node.next = self.head
            tail.next = node
            self.head.prev = node
            self.head = node
            self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        if self.size == 0:
            self.head = node
            self.head.prev = self.head
            self.head.next = self.head
            self.size += 1
        else:
            tail = self.head.prev
            node.prev = tail
            node.next = self.head
            self.head.prev = node
            tail.next = node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        new_node = ListNode(val)
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            node = self.__getNode(index)
            new_node.next = node
            new_node.prev = node.prev
            node.prev.next = new_node
            node.prev = new_node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        node = self.__getNode(index)
        if node is not None:
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
            if index == 0:
                self.head = next
            self.size -= 1


    def printList(self):
        values = []
        p = self.head
        for _ in range(0, self.size):
            values.append(str(p.val))
            p = p.next
        print(','.join(values))


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

if __name__ == '__main__':
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.printList()
    linkedList.addAtIndex(1,2)   # 链表变为1-> 2-> 3
    print(f'this should be 3: {linkedList.get(2)}')
    linkedList.printList()
    print(linkedList.get(1))            # 返回2
    linkedList.deleteAtIndex(1)  # 现在链表是1-> 3
    linkedList.printList()
    print(f'this should be 3: {linkedList.get(1)}')           # 返回3
    print(f'this should be 3: {linkedList.get(-1)}')

    print('------------------------------------------------------------------')
    ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"]
    [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]

    l = MyLinkedList()
    l.addAtHead(2)
    l.deleteAtIndex(1)
    l.printList()

# leetcode submit region end(Prohibit modification and deletion)
