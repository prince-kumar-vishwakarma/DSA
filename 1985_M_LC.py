# 1985. Find the Kth Largest Integer in the Array

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        # min heap se solve karunga
        heap = []
        for n in nums:
            heapq.heappush(heap, int(n))
            if len(heap)>k:
                heapq.heappop(heap)
        return str(heapq.heappop(heap))