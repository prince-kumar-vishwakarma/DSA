# 115. Distinct Subsequences


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        dp = [[-1]*n for _ in range(m)]
        #============= Recursive ==============#
        # def f(i, j):
        #     if j < 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if dp[i][j] != -1: return dp[i][j]
        #     not_take = f(i-1, j)

        #     take = 0
        #     if s[i] == t[j]:
        #         take = f(i-1, j-1)
        #     dp[i][j] = not_take + take
        #     return not_take + take
        # return f(m-1, n-1)

        #============= Iterative ==============#
        for i in range(m):
            for j in range(n):
                take = 0
                if s[i] == t[j]:
                    if j == 0:
                        take = 1
                    elif i == 0:
                        take = 0
                    else:
                        take = dp[i-1][j-1]
                not_take = dp[i-1][j] if i > 0 else 0
                dp[i][j] = not_take + take
        return dp[m-1][n-1]
 
        