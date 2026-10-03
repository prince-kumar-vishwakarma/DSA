# 1482. Minimum Number of Days to Make m Bouquets

class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n<m*k: return -1
        l, r = min(bloomDay), max(bloomDay)
        def bloom(val):
            blo = 0
            temp = 0
            for n in bloomDay:
                if val>=n:
                    temp+=1
                    if temp == k:
                        blo += 1
                        temp = 0
                else:
                    temp = 0
                
            return blo >= m

        while l<=r:
            mid = (l+r)>>1
            if bloom(mid):
                r = mid-1
            else:
                l = mid+1
        return l
        