"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        while queue:
            curr = queue.popleft()
            for neigh in curr.neighbors:
                if neigh not in visited:
                    visited[neigh] = Node(neigh.val, [])
                    queue.append(neigh)
                visited[curr].neighbors.append(visited[neigh])
        return visited[node]