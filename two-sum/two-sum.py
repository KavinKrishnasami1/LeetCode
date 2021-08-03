class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        newdict = {}
        for i in range(len(nums)):
            if nums[i] in newdict:
                return [newdict[nums[i]], i]
            else:
                newdict[target-nums[i]] = i
                