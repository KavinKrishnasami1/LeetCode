class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        self.dict = {}
        if not costs:
            return 0
        
        def helper(n, color):
            if (n, color) in self.dict:
                return self.dict[(n, color)]
            
            cost = costs[n][color]
            if n != len(costs) - 1:
                if color == 0:
                    cost += min(helper(n + 1, 1), helper(n + 1, 2))
                elif color == 1:
                    cost += min(helper(n + 1, 0), helper(n + 1, 2))
                elif color == 2:
                    cost += min(helper(n + 1, 0), helper(n + 1, 1))
            self.dict[(n, color)] = cost
            return cost
        
        return min(helper(0, 0), helper(0, 1), helper(0, 2))