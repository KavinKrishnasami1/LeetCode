class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse = True)

        target = sum(nums) / k
        used = [False] * len(nums)
        cache = {}
        
        def backtrack(i, k, subSum):
            if tuple(used) in cache:
                return cache[tuple(used)]
            if k == 0:
                return True
            if subSum == target:
                partition = backtrack(0, k - 1, 0)
                cache[tuple(used)] = partition
                return partition
            
            for j in range(i, len(nums)):
                if used[j] or (subSum + nums[j] > target):
                    continue
                used[j] = True
                if backtrack(j + 1, k, subSum + nums[j]):
                    return True
                used[j] = False
            
            cache[tuple(used)] = False
            return False
        
        return backtrack(0, k, 0)