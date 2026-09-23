# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans = min_end = max_end = nums[0]
        for i in range(1, len(nums)):
            v1, v2, v3 = nums[i], nums[i]*min_end, nums[i]*max_end
            min_end = min(v1, min(v2,v3))
            max_end = max(v1, max(v2,v3))
            ans = max(ans, min_end, max_end)
        return ans
        