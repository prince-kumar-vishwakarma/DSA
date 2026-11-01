# 766. Largest Subarray with Sum 0

class Solution:
    def maxLen(self, arr):
        hm = {}
        s = 0
        ans = 0
        for i, n in enumerate(arr):
            s += n
            if s == 0:
                ans = max(ans, i+1)
                continue
            if s in hm:
                ans = max(ans, i-hm[s])
            else:
                hm[s] = i
        return ans