# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        dummy = ListNode()
        curr = dummy
        while curr1 or curr2:
            n = 0
            if curr1 and curr2:
                n = curr1.val + curr2.val + carry
            elif curr1:
                n = curr1.val + carry
            elif curr2:
                n = curr2.val + carry
            
            if n >= 10:
                n -= 10
                carry = 1
            else:
                carry = 0
                
            node = ListNode(n)
            curr.next = node
            curr = node
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
            