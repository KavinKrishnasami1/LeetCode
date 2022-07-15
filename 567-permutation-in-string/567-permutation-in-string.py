class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars = {}
        for char in s1:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        left = 0
        right = len(s1)
        while right < len(s2) + 1:
            s = s2[left:right]
            schars = {}
            for char in s:
                if char in schars:
                    schars[char] += 1
                else:
                    schars[char] = 1
            if chars == schars:
                return True
            left += 1
            right += 1
        
        return False