class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {")": "(", "}" : "{", "]": "["}
        
        for char in s:
            if char in chars:
                if stack and stack[-1] == chars[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        if not stack:
            return True
        return False