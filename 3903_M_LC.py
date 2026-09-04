# 3903. Smallest Stable Index I
# https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi = nums[0]
        length = len(nums)
        for i,n in enumerate(nums):
            maxi = max(maxi, n)
            if maxi - min(nums[i:length]) <= k:
                return i
        return -1

