# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x,y):
            return math.sqrt(x**2 + y**2)
        heap = []
        for point in points:
            heapq.heappush(heap, (distance(point[0], point[1]), point))
            
        return [heapq.heappop(heap)[1] for _ in range(k)]