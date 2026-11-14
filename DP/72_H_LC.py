# 72. Edit Distance


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[-1]*n for _ in range(m)]
        # def f(i, j):
        #     if i<0 or j<0:
        #         return 1 + max(i, j)

        #     if word1[i] == word2[j]:
        #         return 0 + f(i-1, j-1)
        #     if dp[i][j] != -1: return dp[i][j]
            
        #     delete = 1 + f(i-1, j)
        #     replace = 1 + f(i-1, j-1)
        #     insert = 1 + f(i, j-1)
        #     dp[i][j] = min(delete, replace, insert)
        #     return dp[i][j]
        # return f(m-1, n-1)

        dp = [[0]*(n+1) for _ in range(m+1)]
        # Base cases
        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = 0 + dp[i-1][j-1]
                else:
                    delete = 1 + dp[i-1][j]
                    replace = 1 + dp[i-1][j-1]
                    insert = 1 + dp[i][j-1]
                    dp[i][j] = min(delete, replace, insert)
        return dp[m][n]


        