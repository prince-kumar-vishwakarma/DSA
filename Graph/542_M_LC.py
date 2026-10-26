# 542. 01 Matrix

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        visited = [[False]*n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]
            
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
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




        