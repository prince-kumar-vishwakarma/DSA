# 75. Sort Colors


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        i = 0
        while i<=r:
            if nums[i] == 0:
                nums[l],nums[i] = nums[i],nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1


        # dp = [0,0,0]
        # for num in nums:
        #     dp[num] += 1
        
        # idx = 0
        # for i,d in enumerate(dp):
        #     while(d):
        #         nums[idx]=i
        #         idx += 1
        #         d -= 1


        