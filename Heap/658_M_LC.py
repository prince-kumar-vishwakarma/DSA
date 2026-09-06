# 658. Find K Closest Elements
# https://leetcode.com/problems/find-k-closest-elements/description/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(a - x), a) for a in arr]
        heapq.heapify(heap)
        return sorted([heapq.heappop(heap)[1] for _ in range(k)])
        