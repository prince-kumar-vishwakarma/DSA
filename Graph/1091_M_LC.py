# 1091. Shortest Path in Binary Matrix


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        dist = [[10**9]*n for _ in range(n)]
        dist[0][0] = 1
        pq = [(1, 0, 0)]
        while pq:
            d, row, col = heapq.heappop(pq)
            if row == n-1 and col == n-1:
                return dist[n-1][n-1]
            if d > dist[row][col]:
                continue

            for x in range(-1, 2):
                for y in range(-1, 2):
                    nr, nc = row+x, col+y
                    if 0<=nr<n and 0<=nc<n and grid[nr][nc] == 0:
                        if dist[nr][nc] > d+1:
                            dist[nr][nc] = d+1
                            heapq.heappush(pq, (d+1, nr, nc))
        return -1

                        
                