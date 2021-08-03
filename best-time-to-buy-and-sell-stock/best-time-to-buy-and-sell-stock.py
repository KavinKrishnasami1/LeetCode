class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        lowest = prices[0]
        for i in range(1, len(prices)):
            if (prices[i] - lowest) > max:
                max = prices[i] - lowest
            if prices[i] < lowest:
                lowest = prices[i]
                
        return max