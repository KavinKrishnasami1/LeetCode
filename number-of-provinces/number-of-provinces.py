class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)
        return provinces
            