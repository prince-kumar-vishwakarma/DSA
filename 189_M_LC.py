# 189. Rotate Array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate_array(l ,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
        n = len(nums)
        k = k%n
        rotate_array(0,n-k-1)
        rotate_array(n-k, n-1)
        rotate_array(0, n-1)
        
        