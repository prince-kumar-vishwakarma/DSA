
# 714. Frog jump with K distances

class Solution:
    def frogJump(self, heights, k):
        n = len(heights)
        dp = [-1]*n
        def energy(n):
            if n == 0: return 0
            if dp[n] != -1: return dp[n]
            one = energy(n-1) + abs(heights[n]-heights[n-1])
            for i in range(2,k+1):
                two = energy(n-i) + abs(heights[n]-heights[n-i]) if n-i>=0 else float("inf")
                if two == float("inf"): break
                one = min(one, two)
            dp[n] = one
            return one
        return energy(n-1)
                    