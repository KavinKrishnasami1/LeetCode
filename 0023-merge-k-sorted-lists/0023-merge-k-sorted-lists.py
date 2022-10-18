# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        
        if amount > 0:
            return lists[0]
        return None
        
    def merge2Lists(self, l1, l2):
        head = curr = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        if l1:
            while l1:
                curr.next = ListNode(l1.val)
                l1 = l1.next
                curr = curr.next
        elif l2:
            while l2:
                curr.next = ListNode(l2.val)
                l2 = l2.next
                curr = curr.next
        return head.next