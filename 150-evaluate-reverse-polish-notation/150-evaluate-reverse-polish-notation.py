class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        nums = "0123456789"
        for char in tokens:
            val = 0
            if char == "+":
                val = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif char == "-":
                val = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif char == "*":
                val = stack[-2] * stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif char == "/":
                val = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(char))
        
        return stack[-1]