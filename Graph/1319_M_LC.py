# 1319. Number of Operations to Make Network Connected

class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        # totalEdge = len(connections)
        # if not (n-1 <= totalEdge): return -1

        # adj = [[] for _ in range(n)]
        # for u, v in connections:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visited = [False]*n
        # def dfs(u):
        #     visited[u] = True
        #     for v in adj[u]:
        #         if not visited[v]:
        #             dfs(v)
        # component = 0
        # for u in range(n):
        #     if not visited[u]:
        #         component += 1
        #         dfs(u)
        # return component - 1

        ##########--------DSU--------#############
        parent = [i for i in range(n)]
        rank = [0]*n
        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            ulp_u = find(u)
            ulp_v = find(v)
            if ulp_u == ulp_v: return
            if rank[ulp_u]>rank[ulp_v]:
                parent[ulp_v] = ulp_u
            elif rank[ulp_u]<rank[ulp_v]:
                parent[ulp_u] = ulp_v
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1
        extra = 0
        for u, v in connections:
            if find(u) == find(v):
                extra += 1
            else:
                union(u, v)
        components = 0
        for i, u in enumerate(parent):
            if i == u: components += 1

        return components-1 if extra>=components-1 else -1
 
        
        