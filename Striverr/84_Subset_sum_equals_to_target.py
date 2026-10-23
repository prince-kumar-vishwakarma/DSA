# 84. Subset sum equals to target

class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        # dp = [[-1]*(target+1) for _ in range(n+1)]
        # def f(i, target):
        #     if target == 0: return True
        #     if target < 0: return False
        #     if i == 0: return arr[i] == target

        #     if dp[i][target] != -1: return 1 == dp[i]
        #     nT = f(i-1, target)
        #     T = False
        #     if target >= arr[i]:
        #         T = f(i-1, target-arr[i])

        #     res = nT or T
        #     dp[i][target] = 1 if res else 0
        #     return res
        # return f(n-1, target)

        dp = [[False]*(target+1) for _ in range(n+1)]

        for i in range(n):
            dp[i][0] = True
        if arr[0] <= target:
            dp[0][arr[0]] = True

        for i in range(1, n):
            for tar in range(target+1):
                not_take = dp[i - 1][tar]
                take = False

                if arr[i] <= tar:
                    take = dp[i - 1][tar - arr[i]]

                dp[i][tar] = take or not_take
        return dp[n-1][target]


     