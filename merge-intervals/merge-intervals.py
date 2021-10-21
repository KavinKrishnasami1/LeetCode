class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = []
        for pair in intervals:
            if not output or pair[0] > output[-1][1]:
                output.append(pair)
            elif pair[0] <= output[-1][1]:
                if pair[1] > output[-1][1]:
                    output[-1][1] = pair[1]
        
        return output
        