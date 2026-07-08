class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        max_p = 0
        min_p = float("inf")
        for i in range(0,n):
            min_p = min(min_p,prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p