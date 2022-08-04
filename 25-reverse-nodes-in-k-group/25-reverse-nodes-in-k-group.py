# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            newK = self.getK(groupPrev, k)
            if not newK:
                break
            groupNext = newK.next
            prev, curr = newK.next, groupPrev.next
            while curr != groupNext:
                hold = curr.next
                curr.next = prev
                prev = curr
                curr = hold
            
            temp = groupPrev.next
            groupPrev.next = newK
            groupPrev = temp
            
        return dummy.next
            
    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr