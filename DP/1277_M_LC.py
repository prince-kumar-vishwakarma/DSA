# 1277. Count Square Submatrices with All Ones

class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return sum([sum(s) for s in dp])
        