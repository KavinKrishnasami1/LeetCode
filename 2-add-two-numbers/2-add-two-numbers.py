# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1 = l1
        c2 = l2
        carry = 0
        dummy = ListNode()
        curr = dummy
        while c1 or c2:
            if c1 and c2:
                n = c1.val + c2.val + carry
            elif c1:
                n = c1.val + carry
            elif c2:
                n = c2.val + carry
            if n >= 10:
                n -= 10
                carry = 1
            else:
                carry = 0
            node = ListNode(n)
            curr.next = node
            curr = node
            if c1:
                c1 = c1.next
            if c2:
                c2 = c2.next
        
        if carry:
            node = ListNode(carry)
            curr.next = node

        return dummy.next
            
            