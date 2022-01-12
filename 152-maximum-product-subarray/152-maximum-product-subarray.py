class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = max(nums)
        curMin, curMax = 1, 1
        
        for num in nums:
            tmp = curMax
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(num * tmp, num * curMin, num)
            output = max(output, curMax)
        
        return output