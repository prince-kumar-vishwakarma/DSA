# 138. Find the repeating and missing number

class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        sn = n*(n+1)//2
        s = sum(nums)
        xsy = s-sn
        sn = n*(n+1)*(2*n+1)//6
        s = 0
        for n in nums:
            s += n**2
        xpy = (s - sn)//xsy
        x = (xsy+xpy)//2
        y = x - xsy
        return x, y