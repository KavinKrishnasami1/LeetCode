class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_dict = {}
        j = 0
        k = 0
        for i in range(len(s)):
            if s[i] not in new_dict:
                new_dict[s[i]] = i
            else:
                j = max(j, new_dict[s[i]] + 1)
                new_dict[s[i]] = i
            k = max(k, i - j + 1)
        
        return k
                
                    