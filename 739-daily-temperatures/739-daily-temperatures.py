class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #[temp, index]
        
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop()
                output[index] = i - index
            stack.append(i)
        
        return output
                