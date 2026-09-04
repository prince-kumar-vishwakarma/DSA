# 3876. Construct Uniform Parity Array II
# https://leetcode.com/problems/construct-uniform-parity-array-ii

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        have_odd = False
        smallest_num = nums1[0]
        for n in nums1:
            if n&1:
                have_odd = True
            smallest_num = min(smallest_num, n)

        if have_odd and smallest_num&1 == 0:
            return False
        return True
        


