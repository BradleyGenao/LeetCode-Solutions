class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preqs = defaultdict(set)
        in_degrees = defaultdict(int)
        {preqs[nxt].add(pre) for nxt, pre in prerequisites }
        {in_degrees[i] for i in range(numCourses)}
        for _, pre in prerequisites:
            in_degrees[pre] +=1
        queue = deque()
        seen = set()
        for index, in_degree in in_degrees.items():
            if in_degree == 0:
                queue.append(index)
        while queue:
            cur_crse = queue.popleft()
            seen.add(cur_crse)
            for neigh in preqs[cur_crse]:
                in_degrees[neigh] -=1
                if in_degrees[neigh] == 0:
                    queue.append(neigh)
        return len(seen) == numCourses

        