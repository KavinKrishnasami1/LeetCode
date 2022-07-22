class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1
        
        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        
        if top > bot:
            return False
        
        i = (top + bot) // 2
        l = 0
        r = len(matrix[i]) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[i][mid]:
                l = mid + 1
            elif target < matrix[i][mid]:
                r = mid - 1
            else:
                return True
        
        return False
        