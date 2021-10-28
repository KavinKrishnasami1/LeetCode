# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            total = 0
            if root.val >= maxVal:
                total = 1
            maxVal = max(maxVal, root.val)
            total += dfs(root.left, maxVal)
            total += dfs(root.right, maxVal)
            return total
        
        return dfs(root, -100000)