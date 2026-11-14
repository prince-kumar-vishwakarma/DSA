# 115. Distinct Subsequences


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[-1]*n for _ in range(m)]

        def f(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1: return dp[i][j]
            not_take = f(i-1, j)

            take = 0
            if s[i] == t[j]:
                take = f(i-1, j-1)
            dp[i][j] = not_take + take
            return not_take + take
        return f(m-1, n-1)

        
        