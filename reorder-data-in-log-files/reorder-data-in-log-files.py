class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        output = []
        for log in logs:
            parts = log.split(" ")
            if parts[1].isdigit():
                digits.append(parts)
            else:
                letters.append(parts)
                
        letters.sort(key = lambda x : (x[1:],x[0]))
        for letter in letters:
            output.append(letter)
        for digit in digits:
            output.append(digits)
            
        return [" ".join(l) for l in letters] + [" ".join(d) for d in digits]