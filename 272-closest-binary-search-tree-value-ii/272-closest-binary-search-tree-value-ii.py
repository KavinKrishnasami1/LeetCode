# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def helper(node):
            if node:
                return helper(node.left) + [node.val] + helper(node.right)
            else:
                return []
        
        vals = helper(root)
        vals.sort(key = lambda x:abs(x - target))
        
        return vals[0:k]