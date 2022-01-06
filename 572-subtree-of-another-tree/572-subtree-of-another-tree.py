# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            return r.val == s.val and isSame(r.left, s.left) and isSame(r.right, s.right)
        
        def helper(r, s):
            if isSame(r, s):
                return True
            if not r or not s:
                return False
            return helper(r.left, s) or helper(r.right, s)
        
        return helper(root, subRoot)