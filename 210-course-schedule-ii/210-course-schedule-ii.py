class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        {graph[pre].append(crse) for crse, pre in prerequisites }
        
        for i in range(numCourses):
            for edge in graph[i]:
                in_degrees[edge] +=1
        ans, queue = [], deque()
        
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            
            for neigh in graph[curr]:
                in_degrees[neigh] -=1
                if in_degrees[neigh] == 0:
                    queue.append(neigh)
        return ans if len(ans) == numCourses else []
        
        
        
        
        
        