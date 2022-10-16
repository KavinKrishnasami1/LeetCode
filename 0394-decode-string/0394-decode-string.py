class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curString = ""
        curNum = 0
        
        for char in s:
            if char == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
            elif char == ']':
                num = stack.pop()
                prev = stack.pop()
                curString = prev + (num * curString)
            elif char.isdigit():
                curNum = (curNum * 10) + int(char)
            else:
                curString += char
                
        return curString