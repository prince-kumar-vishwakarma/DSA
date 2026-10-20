# 931. Minimum Falling Path Sum

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        # dp = [[-1]*n for _ in range(n)]

        # def f(i, j):
        #     if j<0 or j>=n: return float("inf")
        #     if i == 0: return matrix[0][j]
        #     if dp[i][j] != -1: return dp[i][j]
        #     left = f(i-1, j-1)
        #     same = f(i-1, j)
        #     right = f(i-1, j+1)
        #     dp[i][j] = matrix[i][j] + min(left, same, right)
        #     return dp[i][j]
        # best = float("inf")
        # for i in range(n):
        #     best = min(best, f(n-1, i))
        # return best

        # dp = [[-1]*n for _ in range(n)]
        # best = float("inf")
        # for i in range(n):
        #     dp[0][i] = matrix[0][i]
        # for i in range(1, n):
        #     for j in range(n):
        #         left = dp[i-1][j-1] if j>0 else float("inf")
        #         right = dp[i-1][j+1] if j<n-1 else float("inf")
        #         dp[i][j] = matrix[i][j] + min(left, right, dp[i-1][j])
        # return min(dp[n-1])

        dp = matrix[0][:]
        for i in range(1, n):
            temp = [-1]*n
            for j in range(n):
                left = dp[j-1] if j>0 else float("inf")
                right = dp[j+1] if j<n-1 else float("inf")
                temp[j] = matrix[i][j] + min(left, right, dp[j])
            dp = temp
        return min(dp)


        