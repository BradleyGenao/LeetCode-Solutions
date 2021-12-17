# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
      
        def dfs(node):
            if not node:
                return 0
            if not node.left:
                return dfs(node.right) + 1
            if not node.right:
                return dfs(node.left) + 1
            return min(dfs(node.left), dfs(node.right)) + 1
        return dfs(root)
            
        