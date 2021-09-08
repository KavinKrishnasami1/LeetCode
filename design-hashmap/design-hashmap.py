class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        exists = False
        for pair in self.list:
            if pair[0] == key:
                pair[1] = value
                exists = True
                
        if not exists:
            self.list.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for pair in self.list:
            if pair[0] == key:
                return pair[1]
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for i in range(len(self.list)):
            if self.list[i][0] == key:
                self.list.pop(i)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)