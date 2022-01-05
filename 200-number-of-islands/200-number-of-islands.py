class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0":
                return 0
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs (i, j + 1)
            dfs(i, j - 1)
            return 1
        
        if grid == None or len(grid) == 0:
            return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                num += dfs(i, j)
        return num
            