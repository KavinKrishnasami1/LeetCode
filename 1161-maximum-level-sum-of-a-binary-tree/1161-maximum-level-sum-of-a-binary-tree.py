# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def inorder(node, level):
            if node:
                inorder(node.left, level + 1)
                new_dict[level] += node.val
                inorder(node.right, level + 1)
        
        new_dict = defaultdict(int)
        inorder(root, 1)
        
        return max(new_dict, key = lambda level: (new_dict[level], -level))