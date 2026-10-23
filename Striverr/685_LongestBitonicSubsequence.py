# 685. Longest Bitonic Subsequence

class Solution:
    def LongestBitonicSequence(self, arr):
        n = len(arr)
        dp1 = [1]*n
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j] and dp1[i]<dp1[j]+1:
                    dp1[i] = dp1[j]+1
        dp2 = [1]*n
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if arr[i]>arr[j] and dp2[i]<dp2[j]+1:
                    dp2[i] = dp2[j]+1
        ans = 0
        for i in range(n):
            ans = max(ans, dp1[i]+dp2[i]-1)
        return ans


      