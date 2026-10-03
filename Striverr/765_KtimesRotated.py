# 765. Find out how many times the array is rotated

class Solution:
    def findKRotation(self, nums):
        n = len(nums)
        l, r  = 0, n-1
        minIdx = -1
        mini = float("+inf")
        while l<=r:
            mid = (l+r)>>1
            if nums[l]<=nums[r]:
                if mini>nums[l]:
                    mini = nums[l]
                    minIdx = l
                break

            if nums[l]<=nums[mid]:
                if mini>nums[l]:
                    mini = nums[l]
                    minIdx = l
                l = mid+1
            else:
                if mini>nums[mid]:
                    mini = nums[mid]
                    minIdx = mid
                r = mid-1
            
        return minIdx
