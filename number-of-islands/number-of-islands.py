class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        
        def explore(row, col):
            if 0<=row<m and 0<=col<n and grid[row][col] == '1':
                grid[row][col] = '0'
                explore(row-1, col)
                explore(row+ 1, col)
                explore(row, col-1)
                explore(row, col+ 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    explore(i, j)
                    island_count +=1
        return island_count
        