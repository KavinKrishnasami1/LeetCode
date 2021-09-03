class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict.move_to_end(key, last = False)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        self.dict.move_to_end(key, last = False)
        if len(self.dict) > self.capacity:
            self.dict.popitem(last = True)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)