class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        if n ==1 or not edges:
            return [0]
        if n ==2 and len(edges) == 1:
            return edges[0]
        
        
        graph = defaultdict(list)
        in_degrees = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degrees[u] +=1
            in_degrees[v] +=1
        queue, ans = deque(), []
        for i in range(n):
            if in_degrees[i] == 1:
                queue.append(i)
                in_degrees[i] -=1
        
        while queue:
            ans.clear()
        
            for i in range(len(queue)):
                curr = queue.popleft()
                ans.append(curr)
                for neigh in graph[curr]:
                    in_degrees[neigh] -=1
                    if in_degrees[neigh] == 1:
                        queue.append(neigh)
        return ans if ans else [0]
        
        
        
        