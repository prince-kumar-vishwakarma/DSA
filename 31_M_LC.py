# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        break_point = -1
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break_point = i
                break
        if break_point == -1:
            nums.sort()
            return
        just_greater = i+1

        for i in range(n-1, break_point, -1):
            if nums[break_point] < nums[i]:
                just_greater = just_greater if nums[just_greater] < nums[i] else i

        nums[break_point], nums[just_greater] = nums[just_greater], nums[break_point]
        nums[break_point+1: n] = sorted(nums[break_point+1: n])
        

            


        