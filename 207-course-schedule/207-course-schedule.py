class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(set)
        in_degrees = defaultdict(int)
        
        {graph[preq].add(nxt) for preq, nxt in prerequisites }
        {in_degrees[i] for i in range(numCourses) }
        for _, prev in prerequisites:
            in_degrees[prev] +=1
        queue, seen = deque(), set()
        
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                queue.append(index)
        
        while queue:
            curr = queue.popleft()
            seen.add(curr)
            for neigh in graph[curr]:
                in_degrees[neigh] -=1
                if in_degrees[neigh] == 0:
                    queue.append(neigh)
        return len(seen) == numCourses

        