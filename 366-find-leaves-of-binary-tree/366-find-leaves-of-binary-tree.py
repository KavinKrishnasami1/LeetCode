# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        new_dict = collections.defaultdict(list)
        
        def dfs(node, layer):
            if not node:
                return layer
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            new_dict[layer].append(node.val)
            return layer + 1
        
        dfs(root, 0)
        return new_dict.values()