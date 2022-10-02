"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p2, q2 = p, q
        while p2 != q2:
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = q
            
            if q2.parent:
                q2 = q2.parent
            else:
                q2 = p
        
        return p2
            