class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}
        
        for c, p in prerequisites:
            prereq[c].append(p)
        
        visited = set()
        cycle = set()
        output = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for p in prereq[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output