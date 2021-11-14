# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        """
        Solved by using a queue and a dictionary
        
        key = depth
        value = nodes at that level
        
        At the end i just iterate through the list looking 
        for first leaf
        """
        queue, depth_map = collections.deque([root]), collections.defaultdict(list)
        res = []
        depth = 0
        
        while queue:
            lvl = []
            depth +=1
            for _ in range(len(queue)):
                curr = queue.popleft()
                depth_map[depth].append(curr)
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lvl)
        for key, value in depth_map.items():
            for node in value:
                if not node.left and not node.right:
                    return key
                