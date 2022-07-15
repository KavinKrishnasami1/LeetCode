class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        l = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[i])
            longest = max(longest, i - l + 1)            
        return longest