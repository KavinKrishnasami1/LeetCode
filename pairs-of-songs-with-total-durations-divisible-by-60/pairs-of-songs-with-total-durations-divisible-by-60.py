class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        new_dict = defaultdict(int)
        
        for num in time:
            num %= 60
            count += new_dict[(60 - num) % 60]
            new_dict[num] += 1
        
        return count
            
        
            