# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            tempLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                tempLists.append(self.mergeTwoLists(l1, l2))
            lists = tempLists
            
        return lists[0]
    
    def mergeTwoLists(self, l1, l2):
        output = ListNode(0)
        curr = output
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2
        return output.next
        
            