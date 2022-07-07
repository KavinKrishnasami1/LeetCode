class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        an = "abcdefghijklmnopqrstuvwxyz1234567890"
        while i < j:
            while s[i].lower() not in an and i < j:
                i += 1
            while s[j].lower() not in an and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            
        return True