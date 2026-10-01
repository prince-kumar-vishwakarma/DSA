# 45. Jump Game II

class Solution:
    def jump(self, nums: list[int]) -> int:
        l, r = 0, 0
        jump = 0
        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(nums[i]+i, far)
            l = r+1
            r = far
            jump+=1
        return jump
