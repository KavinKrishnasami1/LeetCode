class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
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
        
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    num += dfs(i, j)
        return num