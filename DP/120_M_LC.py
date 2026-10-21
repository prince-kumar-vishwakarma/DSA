# 120. Triangle

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        # dp = [[-1]*n for _ in range(n)]
        # def f(n, i):
        #     if n == 0: return triangle[0][0]
        #     if i<0 or i>=n: return float("inf") 
        #     if dp[n][i] != -1: return dp[n][i]
        #     cur = f(n-1, i)
        #     nxt = f(n-1, i-1)
        #     dp[n][i] = triangle[n][i] + min(cur, nxt)
        #     return dp[n][i]
        # best = float("inf")
        # for i in range(n):
        #     best = min(best,f(n-1, i))
        # return best

        # ------------ Iterative ---------------
        dp = triangle[0][:]
        for i in range(1,n):
            temp = [0]*(i+1)
            for j in range(i+1):
                left = dp[j-1] if j>0 else float("inf")
                right = dp[j] if j<i else float("inf")
                temp[j] = triangle[i][j] + min(left, right) 
            dp = temp
        return min(dp)



        