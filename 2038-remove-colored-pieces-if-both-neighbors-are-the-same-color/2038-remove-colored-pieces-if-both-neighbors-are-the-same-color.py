class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        countA = countB = 0
        
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] == colors[i + 1]:
                if colors[i] == "A":
                    countA += 1
                else:
                    countB += 1
        
        return countA > countB