# 309. Best Time to Buy and Sell Stock with Cooldown

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        # dp = [[[-1]*2 for _ in range(2)] for _ in range(n)]
        # def f(i, buy, cooldown):
        #     if i == n: return 0
        #     if dp[i][buy][cooldown] != -1: return dp[i][buy][cooldown]
        #     profit = 0
        #     if buy == 1:
        #         if cooldown == 1:
        #             profit = f(i+1, 1, 0)
        #         else:
        #             profit = max(-prices[i] + f(i+1, 0, 0), f(i+1, 1, 0))
        #     else:
        #         profit = max(prices[i] + f(i+1, 1, 1), f(i+1, 0, 0))
        #     dp[i][buy][cooldown] = profit
        #     return profit
        # return f(0, 1, 0)

        #==================================================
        # dp = [[[0]*2 for _ in range(2)] for _ in range(n+1)]
        # for i in range(n-1, -1, -1):
        #     for buy in range(1, -1, -1):
        #         for cooldown in range(1, -1, -1):
        #             if buy == 1:
        #                 if cooldown == 1:
        #                     dp[i][buy][cooldown] = dp[i+1][1][0]
        #                 else:
        #                     dp[i][buy][cooldown] = max(-prices[i] + dp[i+1][0][0], dp[i+1][1][0])
        #             else:
        #                 dp[i][buy][cooldown] = max(prices[i] + dp[i+1][1][1], dp[i+1][0][0])
        # return dp[0][1][0]

        ahead = [[0]*2 for _ in range(2)]
        for i in range(n-1, -1, -1):
            cur = [[0]*2 for _ in range(2)]
            for buy in range(1, -1, -1):
                for cooldown in range(1, -1, -1):
                    if buy == 1:
                        if cooldown == 1:
                            cur[buy][cooldown] = ahead[1][0]
                        else:
                            cur[buy][cooldown] = max(-prices[i] + ahead[0][0], ahead[1][0])
                    else:
                        cur[buy][cooldown] = max(prices[i] + ahead[1][1], ahead[0][0])
            ahead = cur
        return ahead[1][0]
