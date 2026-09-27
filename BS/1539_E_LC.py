# 1539. Kth Missing Positive Number

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l<=r:
            mid = (l+r)//2
            missing = arr[mid]-(mid+1)
            if missing>=k:
                r = mid - 1
            else:
                l = mid + 1
        return l+k