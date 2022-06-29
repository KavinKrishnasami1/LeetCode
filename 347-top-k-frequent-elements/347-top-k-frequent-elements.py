class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        for num in nums:
            if num in new_dict:
                new_dict[num] += 1
            else:
                new_dict[num] = 1
        
        count = [[] for i in range(len(nums) + 1)]
        
        for num in new_dict:
            count[new_dict[num]].append(num)
        
        output = []
        for i in range(len(nums), -1, -1):
            for num in count[i]:
                output.append(num)
            if len(output) == k:
                return output
            