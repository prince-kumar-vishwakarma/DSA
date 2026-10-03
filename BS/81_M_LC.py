# 81. Search in Rotated Sorted Array II

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)>>1
            if nums[mid] == target: return True
            elif nums[l] == nums[mid] == nums[r]:
                l+=1
                r-=1
            elif nums[mid]>=nums[l]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return False

        