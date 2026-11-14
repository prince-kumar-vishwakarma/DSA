# 1092. Shortest Common Supersequence 


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        text1 = str1
        text2 = str2
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
        lcsLen = dp[m][n]
        lcs = ['$']*lcsLen
        while i>0 and j>0:
            if text1[i-1] == text2[j-1]:
                lcs[lcsLen-1] = text1[i-1]
                lcsLen -= 1
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                i -=1 
            else: j-=1
        
        lcsLen = dp[m][n]
        lcs = "".join(lcs)
        # shortestLen = m + n - lcsLen
        ans = []
        i = j = 0
        for ch in lcs:
            while text1[i] != ch:
                ans.append(text1[i])
                i += 1
            while text2[j] != ch:
                ans.append(text2[j])
                j += 1
            ans.append(ch)
            i += 1
            j += 1
        ans.extend(text1[i:] + text2[j:])
        # ans = "".join(ans)
        # ans += text1[i:]
        # ans += text2[j:]
        return "".join(ans)
        
            
            


        