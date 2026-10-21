# 741. Cherry Pickup

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        # if grid[0][0] == -1: return 0
        n = len(grid)
        dp = [[[[-1]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def f(i1, j1, i2, j2):
            # Overflow
            if i1>=n or j1>=n or i2>=n or j2>=n:
                return float("-inf")
            # Block
            if grid[i1][j1] == -1 or grid[i2][j2] == -1:
                return float("-inf")
            #End
            if dp[i1][j2][i2][j2] != -1: return dp[i1][j2][i2][j2]

            q1 = grid[i1][j1]
            q2 = grid[i2][j2]
            cherries = 0
            if i1 == i2 and j1 == j2:
                if i1 == n-1 and j1 == n-1:
                    return grid[i1][j1]
                cherries += grid[i1][j1]
                grid[i1][j1] = 0
            else:
                cherries += (grid[i1][j1] + grid[i2][j2])
                grid[i1][j1] = 0
                grid[i2][j2] = 0
            
            
            p1 = f(i1+1, j1, i2+1, j2)
            p2 = f(i1+1, j1, i2, j2+1)
            p3 = f(i1, j1+1, i2+1, j2)
            p4 = f(i1, j1+1, i2, j2+1)
            grid[i1][j1] = q1
            grid[i2][j2] = q2

            dp[i1][j2][i2][j2] = cherries + max(p1, p2, p3, p4)
            return dp[i1][j2][i2][j2]
            
        return max(0, f(0,0,0,0))


        