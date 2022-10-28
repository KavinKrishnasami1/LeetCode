class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        l = len(palindrome)
        if l == 1:
            return ""
        k = l // 2
        for i in range(k):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        return palindrome[:-1] + 'b'
