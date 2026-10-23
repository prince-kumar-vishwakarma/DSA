# 673. Number of Longest Increasing Subsequence


class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n
        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
            maxi = max(maxi, dp[i])
        ans = 0
        for i in range(n):
            if dp[i] == maxi:
                ans += cnt[i]

        return ans