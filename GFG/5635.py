# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/

import heapq
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        heapq.heapify(arr)
        for _ in range(k-1):
            heapq.heappop(arr)
        return heapq.heappop(arr)
