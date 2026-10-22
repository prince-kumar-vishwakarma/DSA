# 368. Largest Divisible Subset



class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        dp = [1]*n
        hsh = list(range(n))
        idx = 0
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    hsh[i] = j
            if dp[i] > dp[idx]:
                idx = i
        ans = []
        while idx != hsh[idx]:
            ans.append(nums[idx])
            idx = hsh[idx]
        ans.append(nums[idx])
        return ans
                
        