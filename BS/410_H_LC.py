# 410. Split Array Largest Sum

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k==len(nums):
            return max(nums)
        def find(mid):
            part = 0
            s = 0
            for n in nums:
                if s+n > mid:
                    s = 0
                    part += 1
                s += n
            part+=1  
            return part<=k

        l, r = max(nums), sum(nums)
        while l<=r:
            mid = (l+r)>>1
            if find(mid):
                r = mid-1
            else:
                l = mid+1
        return l




        