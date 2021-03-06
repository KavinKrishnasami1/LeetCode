class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if not self.head:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = ListNode(val)
        if self.size == 0:
            self.head = node
        else:           
            curr = self.head
            for i in range(self.size - 1):
                curr = curr.next
            curr.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size or index < 0:
            return
        else:
            node = ListNode(val)
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            second = curr.next
            curr.next = node
            node.next = second
            self.size += 1
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.head
        if index == 0:
            self.head = curr.next
            curr.next = None
        elif index >= self.size or index < 0:
            return
        else:
            for i in range(index - 1):
                curr = curr.next
            if (curr.next and curr.next.next):
                curr.next = curr.next.next
            else:
                curr.next = None
        self.size -= 1
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)