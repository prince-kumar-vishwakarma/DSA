# 714. Best Time to Buy and Sell Stock with Transaction Fee


class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        n = len(prices)
        dp = [0,0]
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                if buy == 1:
                    dp[buy] = max(dp[0]-prices[i], dp[1])
                else:
                    dp[buy] = max(prices[i] + dp[1] - fee, dp[0])
    
        return dp[1]
        