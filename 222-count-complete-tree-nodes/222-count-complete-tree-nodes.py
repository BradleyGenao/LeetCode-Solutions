# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        
        def get_height(node):
            if not node:
                return 0
            return get_height(node.left) + 1
        
        def count_nodes(node):
            
            
            h = get_height(node)
            if h == 0:
                return 0
            if h-1 == get_height(node.right):
                return 2 **(h-1) + count_nodes(node.right)
            else:
                return 2 **(h-2) + count_nodes(node.left)
            
        
        
        
        return count_nodes(root)
        