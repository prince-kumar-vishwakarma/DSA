# 463. Island Perimeter

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        ans = 0
        n = len(grid)
        m = len(grid[0])
        def dfs(i,j):
            para = 4
            grid[i][j] = 2
            for x,y in directions:
                nx,ny = x+i,y+j
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]:
                    para -= 1
                    if grid[nx][ny] == 1:
                        dfs(nx,ny)
            nonlocal ans
            ans += para

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return ans





        