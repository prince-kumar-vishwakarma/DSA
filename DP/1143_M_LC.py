# 1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        longest = dp[m][n]
        return longest
        
        s = ["$"]*longest
        i, j = m, n
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                s[longest-1] = text1[i-1]
                longest -= 1
                j -= 1
                i -= 1
            elif dp[i-1][j]>dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return "".join(s)


        