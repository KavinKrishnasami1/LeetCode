class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for x, y in prerequisites:
            graph[x].append(y)
        
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            
            visited[node] = -1
            for req in graph[node]:
                if not dfs(req):
                    return False
            visited[node] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
            