class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dict = {}
        i = 0
        for num in sorted(arr):
            if not dict.get(num):
                i += 1
                dict[num] = i
                
        for i in range(len(arr)):
            arr[i] = dict[arr[i]]
            
        return arr