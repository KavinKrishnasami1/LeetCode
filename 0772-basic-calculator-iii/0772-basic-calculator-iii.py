class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        def operation(op, second, first):
            if op == "+":
                return first + second
            elif op == "-":
                return first - second
            elif op == "*":
                return first * second
            elif op == "/":
                return int(first / second)
            
        
        def precedence(curr):
            if curr in "+-":
                return 1
            elif curr in "*/":
                return 2
            return 0
            
        ops = []
        nums = []
        i = 0
        prev = False
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            if s[i].isdigit():
                end = i + 1
                while end < len(s) and s[end].isdigit():
                    end += 1
                nums.append(int(s[i:end]))
                i = end
                prev = True
            elif s[i] in "+-*/":
                if not prev:
                    nums.append(0)
                while ops and precedence(ops[-1]) >= precedence(s[i]):
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.append(s[i])
                i += 1
            elif s[i] == "(":
                ops.append(s[i])
                i += 1
                prev = False
            else:
                while ops[-1] != "(":
                    nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
                ops.pop()
                i += 1
        
        while ops:
            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
        
        return nums[-1]
