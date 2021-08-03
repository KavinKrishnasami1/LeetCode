class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = len(nums)
        for index,value in enumerate(nums):
            answer ^= index^value
            
        return answer