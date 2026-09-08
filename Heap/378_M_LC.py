# 378. Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for mat in matrix:
            for m in mat:
                heapq.heappush(heap, -m)
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heapq.heappop(heap)
        