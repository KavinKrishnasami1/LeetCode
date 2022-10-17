# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxLength = 0
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left) + 1
            R = dfs(node.right) + 1
            
            if node.left and (node.val) + 1 != node.left.val:
                L = 1
            
            if node.right and (node.val) + 1 != node.right.val:
                R = 1
            
            length = max(L, R)
            self.maxLength = max(self.maxLength, length)
            return length
        
        dfs(root)
        return self.maxLength
        