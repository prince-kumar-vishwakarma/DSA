# 1765. Map of Highest Peak

class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        m, n = len(isWater), len(isWater[0])
        visited = [[False]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]
            
        queue = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append([i, j, 0])
                    visited[i][j] = True

        while len(queue):
            i, j, step = queue.popleft()
            ans[i][j] = step

            for x,y in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+x, j+y
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append([ni, nj, 1+step])
        return ans

        