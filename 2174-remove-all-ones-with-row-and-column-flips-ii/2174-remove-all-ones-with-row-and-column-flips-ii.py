class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        rows = set()
        cols = set()
        self.result = float("inf")
        m = len(grid)
        n = len(grid[0])
        def helper(flips):
            hasOnes = False
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and i not in rows and j not in cols:
                        hasOnes = True
                        rows.add(i)
                        cols.add(j)
                        helper(flips + 1)
                        rows.remove(i)
                        cols.remove(j)
            if not hasOnes:
                self.result = min(self.result, flips)
        
        helper(0)
        return self.result