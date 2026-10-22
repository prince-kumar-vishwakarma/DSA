# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # dp = [[-1]*(n+1) for _ in range(n)]
        # def f(i, last_pick):
        #     if i == n: return 0
        #     col = last_pick + 1
        #     if dp[i][col] != -1: return dp[i][col]
        #     ans = f(i+1, last_pick)
        #     if last_pick == -1 or nums[last_pick] < nums[i]:
        #         ans = max(ans, 1 + f(i+1, i))
        #     dp[i][col] = ans
        #     return ans
        # return f(0, -1)

        # =============================================
        # dp = [[0]*(n+1) for _ in range(n+1)]
        # for i in range(n-1, -1, -1):
        #     for last_pick in range(i-1, -2, -1):
        #         col = last_pick + 1
        #         ans = dp[i+1][col]
        #         if last_pick == -1 or nums[last_pick] < nums[i]:
        #             ans = max(ans, 1 + dp[i+1][i+1])
        #         dp[i][col] = ans
        # return dp[0][0]

        # ===================================================

        dp = [1]*n
        for i in range(1, n):
            add = 0
            for j in range(i):
                if nums[j]<nums[i]:
                    add = max(add, dp[j])
            dp[i] += add
        return max(dp)
                
                
