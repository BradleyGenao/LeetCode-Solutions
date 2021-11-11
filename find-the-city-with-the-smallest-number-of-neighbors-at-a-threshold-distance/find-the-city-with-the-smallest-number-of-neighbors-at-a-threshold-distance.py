
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        """
                
        Step 1: Convert the graph into a adj matrix
        Step 2: Use FLoyd Warsha - Find all pair shortest path
        Step 3: Filter and output the city/vertex

        Complexity: Time O(v^3) Space O(v^2)

        """
        
        matrix = [[math.inf for _ in range(n)] for _ in range(n) ]
      
        for start, end, weight in edges:
            matrix[start][end] = weight
            matrix[end][start] = weight
            
            
            matrix[start][start] = 0
            matrix[end][end] = 0
        
        #Floyd Warshal Algo
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix[k][j] = matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
        
        
        min_count = math.inf
        vertex = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i ==j or matrix[j][i] == math.inf:
                    continue
                if matrix[i][j] <= distanceThreshold:
                    count +=1
            if count <= min_count:
                min_count = count
                vertex = i
        return vertex