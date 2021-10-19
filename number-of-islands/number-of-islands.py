class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        num_islands= 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    self.explore_island(grid, i, j)
                    num_islands +=1
        return num_islands
    
    def explore_island(self, grid, i, j):
        if i < 0 or j < 0 or i >=len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return 
        grid[i][j] = '0'
        self.explore_island(grid, i -1 , j)
        self.explore_island(grid, i + 1, j)
        self.explore_island(grid, i, j - 1)
        self.explore_island(grid, i, j + 1)
        
        