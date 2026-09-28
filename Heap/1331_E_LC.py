# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        heap = [(a, i) for i,a in enumerate(arr)]
        heapq.heapify(heap)
        rank = 0
        last = None
        while heap:
            a, i = heapq.heappop(heap)
            if last != a: rank += 1
            arr[i] = rank
            last = a
        return arr

        