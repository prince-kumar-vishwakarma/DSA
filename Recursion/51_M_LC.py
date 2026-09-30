# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = []
        rowHM = [False]*n
        upperHM = [False]*(2*n - 1)
        lowerHM = [False]*(2*n - 1)
        def isSafe(row, col):
            return rowHM[row] or upperHM[n-1 + col-row] or lowerHM[row+col]
        def solve(col, board):
            arr = []
            if col == n:
                for b in board:
                    arr.append("".join(b))
                ans.append(arr)
                return
            for row in range(n):
                if not isSafe(row, col):
                    board[row][col] = "Q"
                    rowHM[row] = True
                    upperHM[n-1 + col-row] = True
                    lowerHM[row+col] = True
                    solve(col+1, board)
                    board[row][col] = "."
                    rowHM[row] = False
                    upperHM[n-1 + col-row] = False 
                    lowerHM[row+col] = False

        
        board = [["." for _ in range(n)] for _ in range(n)]
        solve(0, board)
        return ans

