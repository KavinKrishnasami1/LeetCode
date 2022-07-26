class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict.get(key, [])
        output = ""
        l, r = 0, len(values) - 1
        
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                output = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return output


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)