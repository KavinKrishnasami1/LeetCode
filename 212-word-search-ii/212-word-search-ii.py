class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        output = []
        root = TrieNode()
        curr = root
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.end = True
        
        visit = set()
        res = set()
        def dfs(i, j, node, word):
            if (i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] not in node.children or (i, j) in visit):
                return
            visit.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if node.end:
                res.add(word)
            
            dfs(i + 1, j, node, word)
            dfs(i - 1, j, node, word)
            dfs(i, j + 1, node, word)
            dfs(i, j - 1, node, word)
            visit.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(i, j, root, "")
                
        return list(res)
                    
                