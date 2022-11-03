"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        dummy = Node(-1)
        prev = dummy
        
        def inorder(node):
            nonlocal prev
            if not node:
                return
            inorder(node.left)
            prev.right = node
            node.left = prev
            prev = node
            inorder(node.right)
            
        inorder(root)
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right