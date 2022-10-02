class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        currMax = nums[0]
        currMin = nums[0]
        maxProd = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            
            tempMax = max(curr, curr * currMax, curr * currMin)
            currMin = min(curr, curr * currMax, curr * currMin)
            
            currMax = tempMax
            maxProd = max(maxProd, currMax, currMin)
            
        return maxProd