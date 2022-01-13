class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0
        while l < r:
            water = (r - l) * min(height[r], height[l])
            maxWater = max(water, maxWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater