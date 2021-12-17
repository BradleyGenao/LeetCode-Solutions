class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edges_list = collections.defaultdict(list)
        
        for a, b in edges:
            edges_list[a].append(b)
            edges_list[b].append(a)
        
        visited = set()
        queue = collections.deque()
        connected = 0
        
        for i in range(n):
            if i in visited: continue
            
            queue.append(i)
            while queue:
                curr = queue.popleft()
                for neigh in edges_list[curr]:
                    if neigh in visited: continue
                    visited.add(neigh)
                    queue.append(neigh)
            connected +=1
        return connected
        
        