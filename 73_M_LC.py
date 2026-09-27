# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row = set()
        col = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for r in row:
            for j in range(n):
                matrix[r][j] = 0
        for c in col:
            for i in range(m):
                matrix[i][c] = 0
