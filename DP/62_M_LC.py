# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)]
        def f(i, j):
            if i<0 or j<0: return 0
            if i == 0 and j == 0: return 1
            if dp[i][j] != -1: return dp[i][j]
            dp[i][j] = f(i-1,j) + f(i,j-1)
            return dp[i][j]
        return f(m-1, n-1)
            
        # ----------- Iterative ------------
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]