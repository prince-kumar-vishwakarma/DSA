# 1976. Number of Ways to Arrive at Destination

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        MOD = 10**9 + 7
        dist = [10**9]*n
        ways = [0] * n
        
        dist[0] = 0
        ways[0] = 1
        pq = [(0,0)]

        while pq:
            t, u = heapq.heappop(pq)
            if t>dist[u]: continue
            
            for v,time in adj[u]:
                newTime = t + time
                if dist[v] > newTime:
                    dist[v] = newTime
                    ways[v] = ways[u]
                    heapq.heappush(pq, (dist[v], v)) 
                elif newTime == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        return ways[n-1]

        