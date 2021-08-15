class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or grid == None:
            return 0
        
        def dfs(i, j):
            if i < 0 or i >= len(grid):
                return 0
            if j < 0 or j >= len(grid[i]):
                return 0
            if grid[i][j] == '0':
                return 0
            
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            
            return 1
            
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    numIslands += dfs(i, j)
                    
        return numIslands
    
