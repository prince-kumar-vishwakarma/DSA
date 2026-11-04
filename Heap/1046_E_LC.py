# 1046. Last Stone Weight


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-1*x for x in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            s1 = -heapq.heappop(heap)
            s2 = -heapq.heappop(heap)
            if s1 != s2:
                heapq.heappush(heap, -abs(s1-s2))
        return -heapq.heappop(heap) if len(heap)==1 else 0
        