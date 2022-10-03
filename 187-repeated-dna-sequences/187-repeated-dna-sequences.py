class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        seen = set()
        output = set()
        
        for i in range(len(s) - 10 + 1):
            subString = s[i:i + 10]
            if subString in seen:
                output.add(subString)
            seen.add(subString)
        
        return output
        