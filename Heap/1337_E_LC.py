# 1337. The K Weakest Rows in a Matrix
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, m in enumerate(mat):
            heapq.heappush(heap, (-m.count(1), -i))
            if len(heap)>k:
                heapq.heappop(heap)
        return [-i for _, i in sorted(heap, reverse=True)]