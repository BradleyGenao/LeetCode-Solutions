# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        queue = deque([root])
        ans = []
        swap = False
        while queue:
            size = len(queue)
            lvl = deque()
            for _ in range(size):
                node = queue.popleft()
                if swap:
                    lvl.appendleft(node.val)
                else:
                    lvl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            swap = not swap
            ans.append(lvl)
        return ans

        