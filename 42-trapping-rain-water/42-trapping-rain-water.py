class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        water = 0
        while l < r:
            if maxL < maxR:
                l += 1
                s = maxL - height[l]
                if s > 0:
                    water += s
                maxL = max(maxL, height[l])
            else:
                r -= 1
                s = maxR - height[r]
                if s > 0:
                    water += s
                maxR = max(maxR, height[r])
        
        return water