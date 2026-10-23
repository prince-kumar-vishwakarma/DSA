# 1048. Longest String Chain

class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key= lambda x: len(x))
        n = len(words)
        dp = [1]*n
        maxi = 1
        def comp(s1, s2):
            if len(s1) != len(s2) + 1: return False
            i = 0
            j = 0
            while i<len(s1) and j<len(s2):
                if s1[i] == s2[j]:
                    j += 1
                i += 1
            return j == len(s2)
            
        for i in range(n):
            for j in range(i-1, -1, -1):
                if len(words[i]) > len(words[j])+1:
                    break
                if comp(words[i], words[j]) and dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
            maxi = max(maxi, dp[i])
        return maxi
