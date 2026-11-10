# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        INF = 10**9
        dist = [[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u,v,wt in edges:
            dist[u][v] = wt
            dist[v][u] = wt
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]!=INF and dist[k][j]!=INF:
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        ans = 0
        mini = INF
        for i in range(n):
            cnt = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    cnt += 1
            if mini>=cnt:
                mini = cnt
                ans = i
        return ans


        