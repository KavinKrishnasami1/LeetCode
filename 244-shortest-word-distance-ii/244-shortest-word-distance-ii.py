class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in self.dict:
                self.dict[wordsDict[i]].append(i)
            else:
                self.dict[wordsDict[i]] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        first = self.dict[word1]
        second = self.dict[word2]
        distance = float("inf")
        w1 = w2 = 0
        while w1 < len(first) and w2 < len(second):
            distance = min(distance, abs(first[w1] - second[w2]))
            if first[w1] < second[w2]:
                w1 += 1
            else:
                w2 += 1
        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)