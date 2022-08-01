"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_dict = {None : None}
        curr = head
        while curr:
            new_dict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            new_dict[curr].next = new_dict[curr.next]
            new_dict[curr].random = new_dict[curr.random]
            curr = curr.next
        
        return new_dict[head]