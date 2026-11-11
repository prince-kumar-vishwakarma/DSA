# 802. Find Eventual Safe States


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        transponse = [[] for _ in range(n)]
        indeg = [0]*n
        for u in range(n):
            for v in graph[u]:
                transponse[v].append(u)
                indeg[u] += 1
        pq = []
        for i,deg in enumerate(indeg):
            if deg == 0:
                pq.append(i)
        ans = []
        while pq:
            node = pq.pop()
            ans.append(node)
            for neigh in transponse[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    pq.append(neigh)
        return sorted(ans)




