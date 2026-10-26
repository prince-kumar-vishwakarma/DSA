# number-of-connected-components-in-an-undirected-graph/description/

class Solution:
    def findNumberOfComponent(self, V, edges):
        G = [[] for _ in range(V)]
        for u, v in edges:
            G[u] = v
            G[v] = u
        visited = [False]*V
        def dfs(root):
            visited[root] = True
            for adj in G[root]:
                if not visited[adj]:
                    dfs(root)
        ans = 0
        for i in range(V):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans
