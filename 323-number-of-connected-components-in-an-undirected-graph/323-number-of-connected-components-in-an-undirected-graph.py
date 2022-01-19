class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        connected = 0
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = set()
        queue = deque()
        for i in range(n):
            if i in seen: continue
            queue.append(i)
            seen.add(i)
            while  queue:
                curr = queue.popleft()
                for neigh in graph[curr]:
                    if neigh in seen: continue
                    queue.append(neigh)
                    seen.add(neigh)
            connected +=1
        return connected

        