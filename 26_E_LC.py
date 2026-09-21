# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        slow = 0
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                slow += 1
                nums[slow] = nums[i]

        return slow+1




        