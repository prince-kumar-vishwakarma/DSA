# 
# 
# 132. Find the MST weight by PRIMS


class Solution:
    def spanningTree(self, V, adj):
        visited = [False]*V
        pq = [(0, 0, -1)]
        mstw = 0
        while pq:
            wt, node, parent = heapq.heappop(pq)
            if visited[node]: 
                continue

            visited[node] = True
            mstw += wt

            for neighbour in adj[node]:
                n, w = neighbour
                if not visited[n]:
                    heapq.heappush(pq, [w, n, node])
        return mstw
                    


    