# 1283. Find the Smallest Divisor Given a Threshold

class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        l, r = 1, max(nums)
        def divideSum(k):
            s = 0
            for n in nums:
                s += math.ceil(n/k)
            return s
        while l<=r:
            mid = (l+r)//2
            sum_ = divideSum(mid)
            if sum_ > threshold:
                l = mid+1
            else:
                r = mid-1
        return l


        