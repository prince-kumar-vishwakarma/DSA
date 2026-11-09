# 948. Articulation point in graph


class Solution:
    def articulationPoints(self, n, adj):
        dt = [-1]*n
        low = [0]*n
        time = 0
        isAP = [False]*n
        def dfs(u, parent):
            nonlocal time
            time += 1
            dt[u] = low[u] = time
            child = 0
            for v in adj[u]:
                if dt[v] == -1:
                    child += 1
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    # AP
                    if parent != -1 and low[v]>=dt[u]:
                        isAP[u] = True

                elif v != parent:
                    low[u] = min(low[u], dt[v])
            if parent == -1 and child>1:
                isAP[u] = True
        for u in range(n):
            if dt[u] == -1:
                dfs(u, -1)

        # ans 
        ans = []
        for i in range(n):
            if isAP[i]:
                ans.append(i)

        return ans if ans else [-1]





        