# 827. Making A Large Island


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        parent = list(range(n*n))
        size = [1]*(n*n)
        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            ulp_u = find(u)
            ulp_v = find(v)
            if ulp_u == ulp_v: return
            if size[ulp_u]>size[ulp_v]:
                parent[ulp_v] = ulp_u
                size[ulp_u] += size[ulp_v]
            elif size[ulp_u]<size[ulp_v]:
                parent[ulp_u] = ulp_v
                size[ulp_v] += size[ulp_u]
            else:
                parent[ulp_v] = ulp_u
                size[ulp_u] += size[ulp_v]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0: continue
                for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                    ni, nj = i+x, j+y
                    if 0<=ni<n and 0<=nj<n and grid[ni][nj] == 1:
                        union(i*n+j, ni*n+nj)
        
        ans = max(
            (size[find(i*n+j)] for i in range(n) for j in range(n)
            if grid[i][j] == 1),
            default=0
        )
        for i in range(n):
            for j in range(n):
                cur = set()
                local_ans = 1
                if grid[i][j] == 0: 
                    for x, y in [(-1,0), (1,0), (0,1), (0,-1)]:
                        ni, nj = i+x, j+y
                        if 0<=ni<n and 0<=nj<n and grid[ni][nj] == 1:
                            u = ni*n+nj
                            ulp_u = find(u)
                            if ulp_u not in cur:
                                cur.add(ulp_u)
                                local_ans += size[ulp_u]          
                ans = max(ans, local_ans)
        return ans
                            



        