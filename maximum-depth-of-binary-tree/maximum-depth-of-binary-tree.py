# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        queue = collections.deque([root])
        
        depths = []
        
        while queue:
            lvl = []
            
            for _ in range(len(queue)):
                curr = queue.popleft()
                lvl.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            depths.append(lvl)
        return len(depths)
                
                
        