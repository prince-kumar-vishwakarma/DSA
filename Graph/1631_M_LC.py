# 1631. Path With Minimum Effort


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        # ------------ queue bfs ------------------
        # row, col = len(heights), len(heights[0])
        # INF = 10**9
        # dp = [[INF]*col for _ in range(row)]
        # dp[0][0] = 0
        # queue = deque([(0,0)])
        # while queue:
        #     r, c = queue.popleft()
        #     for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
        #         nr, nc = r+x, c+y
        #         if 0<=nr<row and 0<=nc<col:
        #             efforts = max(abs(heights[r][c]-heights[nr][nc]), dp[r][c])
        #             if dp[nr][nc] > efforts:
        #                 dp[nr][nc] = efforts
        #                 queue.append((nr, nc))
        # return dp[row-1][col-1]

        #------------Dijkstra --------------
        row, col = len(heights), len(heights[0])
        INF = 10**9
        dp = [[INF]*col for _ in range(row)]
        dp[0][0] = 0
        pq = [(0,0,0)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if r == row-1 and c == col-1:
                return d
            if d>dp[r][c]:
                continue
            for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+x, c+y
                if 0<=nr<row and 0<=nc<col:
                    efforts = max(abs(heights[r][c]-heights[nr][nc]), d)
                    if dp[nr][nc] > efforts:
                        dp[nr][nc] = efforts
                        heapq.heappush(pq, (efforts, nr, nc))
        return -1

        

        