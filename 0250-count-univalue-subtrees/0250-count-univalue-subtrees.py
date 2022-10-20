# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def helper(root):
            if not root:
                return
            left = helper(root.left)
            right = helper(root.right)
            
            if (left is None or left == root.val) and (right is None or right == root.val):
                self.count += 1
                return root.val
            
            return "not uni value"
        
        helper(root)
        return self.count