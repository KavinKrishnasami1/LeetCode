# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = root
        closest = curr.val
        while curr:
            closest = min(closest, curr.val, key = lambda x: abs (x - target))
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        
        return closest