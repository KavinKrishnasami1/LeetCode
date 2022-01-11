class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        k = float("inf")
        while r >= l:
            hours = 0
            m = (r + l) // 2
            for pile in piles:
                if pile <= m:
                    hours += 1
                elif (pile % m) == 0:
                    hours += (pile / m)
                else:
                    hours += ((pile // m) + 1)
            if hours <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k
