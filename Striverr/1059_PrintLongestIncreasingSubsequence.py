# 1059. Print Longest Increasing Subsequence

class Solution:
    def longestIncreasingSubsequence(self, arr):
        n = len(arr)
        dp = [1]*n
        hash_ = list(range(n))
        idx = 0
        for i in range(1, n):
            for j in range(i):
                if arr[i]>arr[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    hash_[i] = j
            if dp[i]>dp[idx]:
                idx = i

        ans = []
        while idx != hash_[idx]:
            ans.append(arr[idx])
            idx = hash_[idx]
        ans.append(arr[idx])
        ans.reverse()
        return ans

        
            


       