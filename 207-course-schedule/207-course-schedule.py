class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        in_degrees = defaultdict(int)
        for i in range(numCourses):
            graph[i].add(i)
            in_degrees[i] = 0 
        for nxt_course, prev_course in prerequisites:
            graph[nxt_course].add(prev_course)
            in_degrees[prev_course] +=1
        
        queue = deque()
        seen = set()
        
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                queue.append(index)
        while queue:
            index = queue.popleft()
            seen.add(index)
            for g in graph[index]:
                in_degrees[g] -=1
                if in_degrees[g] == 0:
                    queue.append(g)
        return len(seen) == numCourses