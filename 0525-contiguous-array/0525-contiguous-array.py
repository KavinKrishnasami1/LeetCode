class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        new_dict = {}
        currSum = 0
        maxLen = 0
        end = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        for i in range(len(nums)):
            currSum += nums[i]
            
            if currSum == 0:
                maxLen = i + 1
                end = i
            
            if currSum in new_dict:
                if maxLen < i - new_dict[currSum]:
                    maxLen = i - new_dict[currSum]
                    end = i
            else:
                new_dict[currSum] = i
        
        return maxLen