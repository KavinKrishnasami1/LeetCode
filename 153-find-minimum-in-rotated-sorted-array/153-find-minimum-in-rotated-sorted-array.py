class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        if nums[r] > nums[l]:
            return nums[0]
        
        while r >= l:
            m = (r + l) // 2
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            if nums[m - 1] > nums[m]:
                return nums[m]
            if nums[m] > nums[l]:
                l = m + 1
            else:
                r = m - 1