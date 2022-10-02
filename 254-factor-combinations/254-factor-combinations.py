class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def dfs(cur, i):
            num = cur.pop()
            while i * i <= num:
                div = num / i
                if num % i == 0:
                    res.append(cur + [i, div])
                    dfs(cur + [i, div], i)
                i += 1
        
        dfs([n], 2)
        return res
            