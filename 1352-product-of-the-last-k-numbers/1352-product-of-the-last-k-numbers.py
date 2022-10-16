class ProductOfNumbers:

    def __init__(self):
        self.list = [1]

    def add(self, num: int) -> None:
        if num != 0:
            self.list.append(self.list[-1] * num)
        else:
            self.list = [1]

    def getProduct(self, k: int) -> int:
        if len(self.list) <= k:
            return 0
        return int(self.list[-1] / self.list[-(k + 1)])