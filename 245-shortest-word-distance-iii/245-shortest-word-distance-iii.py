class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        new_dict = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in new_dict:
                new_dict[wordsDict[i]].append(i)
            else:
                new_dict[wordsDict[i]] = [i]
        
        if word1 == word2:
            sameList = new_dict[word1]
            d = float("inf")
            for i in range(len(sameList) - 1):
                d = min(d, sameList[i + 1] - sameList[i])
            return d
        
        distance = float("inf")
        w1 = w2 = 0
        list1 = new_dict[word1]
        list2 = new_dict[word2]
        while w1 < len(list1) and w2 < len(list2):
            distance = min(distance, abs(list1[w1] - list2[w2]))
            if list1[w1] < list2[w2]:
                w1 += 1
            else:
                w2 += 1
        return distance
                