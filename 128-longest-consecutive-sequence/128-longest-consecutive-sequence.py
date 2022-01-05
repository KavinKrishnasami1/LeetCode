class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        nums.sort()
        maxseq = 0
        seq = 0
        start = nums[0] - 1
        for num in nums:
            if num == start:
                continue
            if num == start + 1:
                seq += 1
                start += 1
            else:
                maxseq = max(maxseq, seq)
                seq = 1
                start = num
        maxseq = max(seq, maxseq)
        return maxseq