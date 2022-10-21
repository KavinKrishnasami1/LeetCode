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
        p1, q1 = p, q
        while p1 != q1:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q
            if q1.parent:
                q1 = q1.parent
            else:
                q1 = p
        
        return p1