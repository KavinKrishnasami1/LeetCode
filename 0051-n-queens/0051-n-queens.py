class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        rightDiag = set() # r + c
        leftDiag = set() # r - c
        
        output = []
        board = [["."] * n for i in range(n)]
        
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                output.append(copy)
                return
            
            for c in range(n):
                if c in cols or (r + c) in rightDiag or (r - c) in leftDiag:
                    continue
                cols.add(c)
                rightDiag.add(r + c)
                leftDiag.add( r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                cols.remove(c)
                rightDiag.remove(r + c)
                leftDiag.remove( r - c)
                board[r][c] = "."
        
        backtrack(0)
        return output