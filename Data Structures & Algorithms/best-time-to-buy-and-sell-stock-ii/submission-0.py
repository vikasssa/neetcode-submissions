class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = - prices[0]
        cash = 0


        for price in prices[1:]:
            prevhold = hold
            prevcash = cash

            hold = max(prevhold, prevcash - price)
            cash = max(prevcash, prevhold + price)
        
        return cash