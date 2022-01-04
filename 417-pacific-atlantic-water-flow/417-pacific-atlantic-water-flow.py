class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(i, j, visit, height):
            if ((i, j) in visit or i < 0 or j < 0 or i >= rows or j >= cols or heights[i][j] < height):
                return
            visit.add((i, j))
            dfs(i + 1, j, visit, heights[i][j])
            dfs(i - 1, j, visit, heights[i][j])
            dfs(i, j + 1, visit, heights[i][j])
            dfs(i, j - 1, visit, heights[i][j])
            
        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows - 1, j, atlantic, heights[rows - 1][j])
            
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])
          
        output = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    output.append([i, j])
        return output

                