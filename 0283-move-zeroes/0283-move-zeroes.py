class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroIndex = 0
        
        for i in range(len(nums)):
            if nums[i] != 0  and nums[zeroIndex] == 0:
                nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i]
            if nums[zeroIndex] != 0:
                zeroIndex += 1
        