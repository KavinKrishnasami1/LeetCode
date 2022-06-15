class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}
        for num in nums:
            if num in new_dict:
                return True
            else:
                new_dict[num] = num
        return False
    