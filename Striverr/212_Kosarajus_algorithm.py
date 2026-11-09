# 212. Kosaraju's algorithm

class Solution:
    def kosaraju(self, V, adj):
        visited = [False]*V
        topo = []
        # Topological Sorting
        def dfs(node, gph):
            visited[node] = True
            for adjNode in gph[node]:
                if not visited[adjNode]:
                    dfs(adjNode, gph)
            topo.append(node)
        transpose = [[] for _ in range(V)]

        for i in range(V):
            if not visited[i]:
                dfs(i, adj)

        # Transpose Graph
        for i in range(V):
            visited[i] = False
            for out in adj[i]:
                transpose[out].append(i)

        # Solution
        def dfs2(node, gph):
            visited[node] = True

            for adjNode in gph[node]:
                if not visited[adjNode]:
                    dfs2(adjNode, gph)
        
        scc = 0
        while topo:
            node = topo.pop()
            if not visited[node]:
                dfs2(node, transpose)
                scc += 1
        return scc
