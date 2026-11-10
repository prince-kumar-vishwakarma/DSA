# 
# 118. Bellman ford algorithm


class Solution:
    def bellman_ford(self, V, edges, S):
        INF = 10**9
        adj = [[] for _ in range(V)]
        for u,v,wt in edges:
            adj[u].append((v, wt))
        dist = [INF]*V
        dist[S] = 0
        for _ in range(V-1):
            changed = False
            for u in range(V):
                for v,wt in adj[u]:
                    if dist[u] != INF and dist[v] > dist[u] + wt:
                        dist[v] = dist[u]+wt
                        changed = True
            if not changed: break
        
        return dist


   