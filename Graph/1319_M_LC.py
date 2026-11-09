# 1319. Number of Operations to Make Network Connected

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        totalEdge = len(connections)
        if not (n-1 <= totalEdge): return -1

        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False]*n
        def dfs(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
        component = 0
        for u in range(n):
            if not visited[u]:
                component += 1
                dfs(u)
        return component - 1
        
        