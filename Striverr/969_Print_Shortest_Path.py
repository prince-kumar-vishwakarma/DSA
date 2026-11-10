# 969. Print Shortest Path


class Solution:
    def shortestPath(self,n, m, edges):
        V = n
        adj = [[] for _ in range(V+1)]
        for u,v,wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))
        
        dist = [10**9]*(V+1)
        dist[1] = 0
        pq = [(0, 1)]
        path = list(range(V+1))
        while pq:
            d, u = heapq.heappop(pq)

            # Skip outdated entries
            if d > dist[u]:
                continue
            
            for v,wt in adj[u]:
                if dist[v] > d + wt:
                    dist[v] = d + wt
                    heapq.heappush(pq, (dist[v], v))
                    path[v] = u
        
        if dist[n] == 10**9:
            return [-1]
        ans = []
        last = n
        while path[last] != 1:
            ans.append(path[last])
            last = path[last]
        ans.append(1)
        ans.reverse()
        return [dist[n]] + ans