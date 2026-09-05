# 3904. Smallest Stable Index II
# https://leetcode.com/problems/smallest-stable-index-ii/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        copy = [0]*n
        mn = float("inf")
        for i in range(n - 1, -1, -1):
            mn = min(mn, nums[i])
            copy[i] = mn

        maxi = nums[0]
        for i,num in enumerate(nums):
            maxi = max(maxi, num)
            if maxi - copy[i] <= k: return i
        return -1

