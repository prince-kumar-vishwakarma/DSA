# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-x for x in nums]
        heapq.heapify(neg)
        for _ in range(k-1):
            heapq.heappop(neg)
        return -1* heapq.heappop(neg)