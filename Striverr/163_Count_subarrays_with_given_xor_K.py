# 163. Count subarrays with given xor K

class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        xr = 0
        hm = {0:1}
        cnt = 0
        for n in nums:
            xr ^= n
            x = xr^k
            cnt += hm.get(x, 0)
            
            hm[xr] = hm.get(xr, 0) + 1
        return cnt