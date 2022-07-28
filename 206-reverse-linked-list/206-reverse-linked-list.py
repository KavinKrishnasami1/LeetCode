# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        curr = head
        second = curr.next
        curr.next = None
        if second == None:
            return head
        
        while second:
            temp = second.next
            second.next = curr
            curr = second
            second = temp
        
        return curr