# 583. Delete Operation for Two Strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1 = word1
        text2 = word2
        if text1 == text2:
            return 0
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp[m][n])
        return len(word1) + len(word2) - 2*dp[m][n]
        