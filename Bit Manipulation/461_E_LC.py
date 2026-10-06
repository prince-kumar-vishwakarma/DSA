# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # cnt = 0
        # while x or y:
        #     if x&1 != y&1:
        #         cnt += 1
        #     x >>= 1
        #     y >>= 1
        # return cnt

        # Another Method
        cnt = 0
        x = x^y
        while x:
            x = x&(x-1)
            cnt+=1
        return cnt
            

        