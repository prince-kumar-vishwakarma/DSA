# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if buy > prices[i]:
                buy = prices[i]
                continue
            profit = max(profit, prices[i]-buy)
        return profit
            
        