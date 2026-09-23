# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        ans = nums[0]
        best_end = nums[0]
        for i in range(1,len(nums)):
            best_end = max(best_end+nums[i], nums[i])
            ans = max(best_end, ans)
        return ans