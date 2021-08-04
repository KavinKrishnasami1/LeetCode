class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        second = []
        for num in nums:
            if num in second:
                return True
            else:
                second.append(num)
        return False