class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        neighbors = collections.defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbors[pattern].append(word)
        
        visited = set()
        visited.add(beginWord)
        q = deque()
        q.append(beginWord)
        total = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return total
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            total += 1
        
        return 0