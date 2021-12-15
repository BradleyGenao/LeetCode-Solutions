# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        diameter = 0
        
        def dia(node):
            if not node:
                return 0
            nonlocal diameter
            left = dia(node.left)
            right = dia(node.right)
            diameter = max(left + right, diameter)
            
            return max(left, right) + 1
        dia(root)
        return diameter
        