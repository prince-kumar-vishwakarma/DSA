#  1192. Critical Connections in a Network


class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        dt = [-1]*n
        low = [0]*n
        time = 0
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        ans = []

        def dfs(v, parent):
            nonlocal time
            time += 1
            dt[v] = time
            low[v] = time

            for u in graph[v]:
                if dt[u] == -1:
                    dfs(u, v)

                    # Update Low
                    low[v] = min(low[v], low[u])

                    # Bridge
                    if low[u] > dt[v]:
                        ans.append([v, u])

                elif u != parent:
                    low[v] = min(low[v], dt[u])
        for i in range(n):
            if dt[i] == -1:
                dfs(i, -1)
        return ans



        