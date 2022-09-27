class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1indices = []
        word2indices = []
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1indices.append(i)
            elif wordsDict[i] == word2:
                word2indices.append(i)
        distance = float("inf")      
        for i in word1indices:
            for j in word2indices:
                distance = min(distance, abs(i - j))
        return distance