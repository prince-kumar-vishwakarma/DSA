# 540. Single Element in a Sorted Array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l , r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if mid+1<len(nums) and nums[mid] == nums[mid+1]:
                if mid&1 == 0:
                    l = mid+2
                else:
                    r = mid-1
            elif mid-1 > -1 and nums[mid-1] == nums[mid]:
                if (mid-1)&1 == 0:
                    l = mid + 1
                else:
                    r = mid - 2
            else:
                return nums[mid]


        