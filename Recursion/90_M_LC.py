# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        def sub(idx, arr):
            ans.append(arr[:])
            for i in range(idx, len(nums)):
                if i>idx and nums[i] == nums[i-1]: continue
                arr.append(nums[i])
                sub(i+1, arr)
                arr.pop()
        sub(0, [])
        return ans
