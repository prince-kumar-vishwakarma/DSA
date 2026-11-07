# 130. Surrounded Regions

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[True]*n for _ in range(m)]
        def dfs(i, j):
            visited[i][j] = False
            for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+x, j+y
                if 0<=ni<m and 0<=nj<n and board[ni][nj] == "O" and visited[ni][nj]:
                    dfs(ni, nj)

        for i in range(m):
            if board[i][0] == "O" and visited[i][0]:
                dfs(i, 0)
            if board[i][n-1] == "O" and visited[i][n-1]:
                dfs(i, n-1)
        for i in range(n):
            if board[0][i] == "O" and visited[0][i]:
                dfs(0, i)
            if board[m-1][i] == "O" and visited[m-1][i]:
                dfs(m-1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and visited[i][j]:
                    board[i][j] = "X"
        

        
        