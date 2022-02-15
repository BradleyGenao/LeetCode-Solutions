# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []
        
        
        
        def get_paths(node, path, curr_sum):
            if not node:
                return 
            path = path + [node.val]
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                paths.append(path)
                return 
            get_paths(node.left, path, curr_sum)
            get_paths(node.right, path, curr_sum)
        
        
    
        get_paths(root, [], 0)
        return paths
        
        
        