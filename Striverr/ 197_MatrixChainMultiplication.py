# 
# 197. Matrix chain multiplication

class Solution:
    def matrixMultiplication(self, nums):
        #your code goes here
        # n = len(nums)
        # dp = [[-1]*n for _ in range(n)]
        # def f(i, j):
        #     if i == j: return 0
        #     if dp[i][j] != -1: return dp[i][j]
        #     ans = float('inf')
        #     for k in range(i, j):
        #         mul = nums[i-1]*nums[k]*nums[j] + f(i, k) + f(k+1, j)
        #         ans = min(ans, mul)
        #     dp[i][j] = ans
        #     return ans
        # return f(1, len(nums)-1)

        dp = [[-1]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(n-1, 0, -1):
            for j in range(i+1, n):
                ans = float("inf")
                for k in range(i, j):
                    mul = nums[i-1]*nums[k]*nums[j] + dp[i][k] + dp[k+1][j]
                    ans = min(ans, mul)
                dp[i][j] = ans
        return dp[1][n-1]


