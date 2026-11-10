# 743. Network Delay Time


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = [[]*(n+1) for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append((v, w))
        INF = 10**9
        dist = [INF]*(n+1)
        dist[k] = 0
        dist[0] = 0
        pq = [(0, k)]
        while pq:
            tt, u = heapq.heappop(pq)
            if tt>dist[u]: continue
            for v, w in adj[u]:
                if dist[v]>dist[u]+w:
                    dist[v]=dist[u]+w
                    heapq.heappush(pq, (dist[v], v))
        print(dist)
        return -1 if max(dist) == INF else max(dist)




        