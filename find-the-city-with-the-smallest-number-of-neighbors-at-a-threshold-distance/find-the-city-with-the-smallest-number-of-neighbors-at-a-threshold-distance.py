
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        """
                
        Step 1: Convert the graph into a adj matrix
        Step 2: Use FLoyd Warsha - Find all pair shortest path
        Step 3: Filter and output the city/vertex

        Complexity: Time O(v^3) Space O(v^2)

        """
        matrix = [[math.inf for _ in range(n)] for _ in range(n)]
        
        for frm, to, weight in edges:
            matrix[to][frm] = weight
            matrix[frm][to] = weight
            
            matrix[to][to] = 0
            matrix[frm][frm] = 0
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    matrix[j][k] = matrix[k][j] = min(matrix[j][k], matrix[i][k] + matrix[i][j])
        
        vertice, min_cost = -1, math.inf
        
        for i in range(n):
            cost = 0
            for j in range(n):
                if i ==j or matrix[i][j] == math.inf: continue
                if matrix[i][j] <= distanceThreshold:
                    cost +=1
            if min_cost >= cost:
                min_cost = cost
                vertice = i
        return vertice
