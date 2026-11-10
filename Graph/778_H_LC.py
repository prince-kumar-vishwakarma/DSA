# 778. Swim in Rising Water


class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]
        INF = 10**9
        dist = [[INF]*n for _ in range(n)] 
        dist[0][0] = grid[0][0]
        while pq:
            maxSwim, r, c = heapq.heappop(pq)
            if r == n-1 and c == n-1:
                return dist[r][c]
            if maxSwim>dist[r][c]: continue

            for x,y in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = r+x, c+y
                if 0<=nr<n and 0<=nc<n:
                    level = max(dist[r][c], grid[nr][nc])
                    if dist[nr][nc]>level:
                        dist[nr][nc] = level
                        heapq.heappush(pq, (level, nr, nc))
        return -1
        

        