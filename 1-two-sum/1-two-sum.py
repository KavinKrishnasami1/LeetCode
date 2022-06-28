class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                return [new_dict[nums[i]], i]
            new_dict[target - nums[i]] = i
            
        
            
            
        