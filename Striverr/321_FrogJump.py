# 321. Frog Jump

class Solution:
    def frogJump(self, heights):
        n = len(heights)
        dp = [-1]*(n)
        def energy(n):
            if n == 0: return 0
            if dp[n] != -1: return dp[n]
            one = energy(n-1) + abs(heights[n]-heights[n-1])
            two = energy(n-2) + abs(heights[n]-heights[n-2]) if n>=2 else float("inf")
            dp[n] = min(one, two)
            return dp[n]
        return energy(n-1)
