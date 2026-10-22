# 188. Best Time to Buy and Sell Stock IV


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        dp = [[[-1]*(k+1) for _ in range(2)] for _ in range(n)]
        def f(i, buy, history):
            if history == 0 or i == n:
                return 0
            if dp[i][buy][history] != -1: return dp[i][buy][history]
            profit = 0
            if buy == 1:
                profit = max(-prices[i] + f(i+1, 0, history), f(i+1, 1, history))
            else:
                profit = max(prices[i] + f(i+1, 1, history-1), f(i+1, 0, history))
            dp[i][buy][history] = profit
            return profit
        return f(0, 1, k)
