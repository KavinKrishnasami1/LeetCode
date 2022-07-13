class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            a = (r - l) * min(height[l], height[r])
            area = max(area, a)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        
        return area