# 1584. Min Cost to Connect All Points


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def manDis(p1, p2):
            return abs(points[p1][0]-points[p2][0]) + abs(points[p1][1]-points[p2][1])
        pq = [(0,0)]
        V = len(points)
        visited = [False]*V
        mstw = 0
        while pq:
            wt, node = heapq.heappop(pq)
            if visited[node]: continue
            visited[node] = True
            mstw += wt
            for i in range(V):
                if not visited[i]:
                    heapq.heappush(pq, (manDis(node, i), i))
        return mstw


        
        