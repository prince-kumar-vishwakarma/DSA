# 733. Flood Fill

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        start_color = image[sr][sc]
        image[sr][sc] = color
        X = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(image)
        n = len(image[0])
        def dfs(i, j):
            for x,y in X:
                nx, ny = x+i, y+j
                if 0<=nx<m and 0<=ny<n and image[nx][ny]==start_color and image[nx][ny]!=color:
                    image[nx][ny] = color
                    dfs(nx, ny)
        dfs(sr,sc)
        return image
        