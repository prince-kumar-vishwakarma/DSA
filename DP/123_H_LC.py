# 123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # n = len(prices)
        # dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]
        # def f(i, buy, history):
        #     if history == 2 or i == n:
        #         return 0
        #     if dp[i][buy][history] != -1: return dp[i][buy][history]
        #     profit = 0
        #     if buy == 1:
        #         p1 = -prices[i] + f(i+1, 0, history)
        #         p2 = f(i+1, 1, history)
        #         profit = max(p1, p2)
        #     else:
        #         p1 = f(i+1, 0, history)
        #         p2 = prices[i] + f(i+1, 1, history+1)
        #         profit = max(p1, p2)
        #     dp[i][buy][history] = profit
        #     return dp[i][buy][history]
        # return f(0, 1, 0)

        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2

        