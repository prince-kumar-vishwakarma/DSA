# 1358. Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [0,0,0]
        ans = 0
        l = 0
        for r in range(n):
            freq[ord(s[r])-ord("a")] += 1
            while freq[0]>0 and freq[1]>0 and freq[2]>0:
                ans += n-r
                freq[ord(s[l])-ord("a")] -= 1
                l+=1
        return ans
