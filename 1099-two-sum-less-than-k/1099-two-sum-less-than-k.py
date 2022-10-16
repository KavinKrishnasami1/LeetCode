class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        output = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if i != j:
                    if nums[i] + nums[j] < k:
                        output = max(output, nums[i] + nums[j])
        
        return output