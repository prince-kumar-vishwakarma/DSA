# 109. Dijkstra's algorithm

class Solution:
    def dijkstra(self, V, edges, S):
        adj = [[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        dist = [10**9]*V
        dist[S] = 0
        pq = [(0, S)]
        while pq:
            d, u = heapq.heappop(pq)

            # Skip outdated entries
            if d > dist[u]:
                continue
            
            for v,wt in adj[u]:
                if dist[v] > d + wt:
                    dist[v] = d + wt
                    heapq.heappush(pq, (dist[v], v))
        return dist


    