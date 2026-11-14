# 44. Wildcard Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[-1]*n for _ in range(m)]
        def f(i, j):
            if j<0 and i<0:
                return True
            if i >= 0 and j < 0:
                return False

            if i<0 and j>=0:
                for k in range(j+1):
                    if p[k] != "*":
                        return False
                return True

            if dp[i][j] != -1: return dp[i][j]

            if s[i] == p[j] or p[j] == "?":
                dp[i][j] =  f(i-1, j-1)
            elif p[j] == "*":
                dp[i][j] =  f(i, j-1) or f(i-1, j)
            else: 
                dp[i][j] = False

            return dp[i][j]
        return f(m-1, n-1)
        