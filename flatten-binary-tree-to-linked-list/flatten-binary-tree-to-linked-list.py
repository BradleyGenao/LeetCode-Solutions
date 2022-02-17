# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = [None]
        
        def dfs(node):
            if not node:
                return None
            dfs(node.right)
            dfs(node.left)
            
            node.right = prev[0]
            node.left = None
            prev[0] = node
        dfs(root)