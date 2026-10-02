class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        minPrice = prices[0]

        for price in prices[1:]:
            if price > minPrice:
                maxProfit = max(maxProfit, price - minPrice)
            else:
                minPrice = price
        
        return maxProfit
        