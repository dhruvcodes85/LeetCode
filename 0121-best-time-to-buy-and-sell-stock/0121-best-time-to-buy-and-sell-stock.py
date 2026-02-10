class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_revenue = 0
        for price in prices:
            if price < min_price:  # Obtained a new minimum price to buy
                min_price = price
            elif price - min_price > max_revenue: # def price is greater than min_price, just calculate the revenue obtained and update if greater
                max_revenue = price - min_price
        return max_revenue