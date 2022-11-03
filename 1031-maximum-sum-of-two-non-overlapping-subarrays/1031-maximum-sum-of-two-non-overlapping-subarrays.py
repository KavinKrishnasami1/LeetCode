class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if firstLen + secondLen > len(nums):
            return 0
        
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        res, maxFirst, maxSecond = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        
        for i in range(firstLen + secondLen, len(nums)):
            maxFirst = max(maxFirst, nums[i - secondLen] - nums[i - secondLen - firstLen])
            maxSecond = max(maxSecond, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, maxFirst + nums[i] - nums[i - secondLen], maxSecond + nums[i] - nums[i - firstLen])
        
        return res
        