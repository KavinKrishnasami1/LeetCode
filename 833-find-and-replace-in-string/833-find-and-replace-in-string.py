class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        output = ""
        res = list(s)
        
        for index, source, target in zip(indices, sources, targets):
            if not s[index:].startswith(source):
                continue
            else:
                res[index] = target
                for i in range(index + 1, len(source) + index):
                    res[i] = ""
        
        return "".join(res)