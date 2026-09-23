# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        suffix = [1]*n
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1]*suffix[i+1]
        pre = 1
        ans = []
        for i in range(n):
            ans.append(suffix[i]*pre)
            pre *= nums[i]
        return ans


        