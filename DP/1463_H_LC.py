# 1463. Cherry Pickup II

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[[-1]*col for _ in range(col)] for _ in range(row)]
        def f(i, j1, j2):
            if j1<0 or j2<0 or j1>=col or j2>= col or i>=row:
                return 0
            if dp[i][j1][j2] != -1: return dp[i][j1][j2]
            if i == row-1:
                if j1 == j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1] + grid[i][j2]
            
            cherries = grid[i][j1]
            if j1 != j2:
                cherries += grid[i][j2]

            best = 0
            for k in range(-1, 2):
                for j in range(-1, 2):
                    best = max(best, f(i+1, j1+k, j2+j))

            dp[i][j1][j2] = best + cherries
            return dp[i][j1][j2]

        return max(0, f(0,0,col-1))