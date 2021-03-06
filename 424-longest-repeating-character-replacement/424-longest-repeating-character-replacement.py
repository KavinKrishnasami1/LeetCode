class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        new_dict = {}
        output = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            new_dict[s[r]] = 1 + new_dict.get(s[r], 0)
            maxf = max(maxf, new_dict[s[r]])
            while (r - l + 1) - maxf > k:
                new_dict[s[l]] -= 1
                l += 1
            output = max(output, r - l + 1)
        
        return output
        