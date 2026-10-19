# 198. House Robber

class Solution:
    def rob(self, nums: list[int]) -> int:
        # n = len(nums)
        # dp = [-1]*n
        # def f(n):
        #     if n==0: return nums[n]
        #     if n<0: return 0
        #     if dp[n] != -1: return dp[n]
        #     first = nums[n] + f(n-2)
        #     second = f(n-1)
        #     dp[n] = max(first, second)
        #     return dp[n]
        # return f(n-1)
        
        prev = prev2 = 0
        for num in nums:
            cur = max(num+prev2, prev)
            prev2 = prev
            prev = cur
        return prev