class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                twoSum = nums[l] + nums[r]
                if twoSum == target:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif twoSum < target:
                    l += 1
                else:
                    r -= 1
        
        return output
                