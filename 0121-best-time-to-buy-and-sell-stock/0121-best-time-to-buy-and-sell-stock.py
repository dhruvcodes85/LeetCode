class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        min = prices[0]
        maxi = prices[0]
        maxRevenue = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[j]:
                min = prices[i]
                j = i
                maxi = prices[j]
            if prices[i] > maxi:
                maxi = prices[i]
            maxRevenue = max(maxRevenue, maxi - min)
        return maxRevenue