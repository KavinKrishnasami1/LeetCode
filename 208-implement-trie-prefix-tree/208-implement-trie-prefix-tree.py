class Trie:

    def __init__(self):
        self.tree = []

    def insert(self, word: str) -> None:
        self.tree.append(word)

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        output = False
        for word in self.tree:
            errors = 0
            if len(prefix) > len(word):
                continue
            for i in range(len(prefix)):
                if prefix[i] != word[i]:
                    errors += 1
            if errors == 0:
                output = True
        return output


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)