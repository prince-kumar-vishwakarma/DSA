# 122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        # dp = [[-1]*2 for _ in range(n)]
        # def f(i, buy):
        #     if i == n: return 0
        #     if dp[i][buy] != -1: return dp[i][buy]
        #     profit = 0
        #     if buy == 1:
        #         p1 = -prices[i] + f(i+1, 0)
        #         p2 = f(i+1, 1)
        #         profit = max(p1,p2)
        #     else:
        #         p3 = f(i+1, 0)
        #         p4 = prices[i] + f(i+1, 1)
        #         profit = max(p3,p4)
        #     dp[i][buy] = profit
        #     return dp[i][buy]
        # return f(0, 1)

        # dp = [[0]*2 for _ in range(n+1)]
        # dp[n][0] = 0
        # dp[n][1] = 0
        # for i in range(n-1, -1, -1):
        #     for buy in range(1, -1, -1):
        #         if buy == 1:
        #             dp[i][buy] = max(-prices[i] + dp[i+1][0], dp[i+1][1])
        #         else:
        #             dp[i][buy] = max(prices[i] + dp[i+1][1], dp[i+1][0])
    
        # return dp[0][1]


        dp = [0,0]
        for i in range(n-1, -1, -1):
            for buy in range(1, -1, -1):
                if buy == 1:
                    dp[buy] = max(-prices[i] + dp[0], dp[1])
                else:
                    dp[buy] = max(prices[i] + dp[1], dp[0])
    
        return dp[1]

        