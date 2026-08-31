# 2091. Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3: return n
        mini, maxi = 0, 0
        for i, num in enumerate(nums):
            if num<nums[mini]:
                mini = i
            if num>nums[maxi]:
                maxi = i
        left = max(mini, maxi) + 1
        right = n - min(mini, maxi)
        both = min(mini, maxi) + 1 + n - max(mini, maxi)
        return min(left, right, both)

        