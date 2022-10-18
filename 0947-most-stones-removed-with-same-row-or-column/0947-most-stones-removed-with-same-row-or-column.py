class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        islands = {}
        
        def find(x):
            if x != islands[x]:
                islands[x] = find(islands[x])
            return islands[x]
        
        def union(x, y):
            islands.setdefault(x, x)
            islands.setdefault(y, y)
            islands[find(x)] = find(y)
        
        for i, j in stones:
            union(i, -(j + 1))
        
        return len(stones) - len({find(x) for x in islands})