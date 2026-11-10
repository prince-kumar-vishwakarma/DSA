# 127. Floyd warshall algorithm


class Solution:
    def shortestDistance(self, matrix):
        INF = 10**9
        V = len(matrix)
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == -1:
                    matrix[i][j] = INF 
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if matrix[i][k] != INF and matrix[k][j] != INF:
                        matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])
        for i in range(V):
            for j in range(V):
                if matrix[i][j] == INF:
                    matrix[i][j] = -1 
        return matrix

    