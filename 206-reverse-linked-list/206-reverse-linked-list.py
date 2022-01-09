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
        temp = curr.next
        if not temp:
            return head
        while temp.next:
            hold = temp.next
            temp.next = curr
            curr = temp
            temp = hold
            
        temp.next = curr
        head.next = None
        head = temp
        return head
            
                        