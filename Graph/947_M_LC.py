# 947. Most Stones Removed with Same Row or Column

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        n = len(stones)
        maxRow = maxCol = 0
        for u,v in stones:
            maxRow = max(maxRow, u)
            maxCol = max(maxCol, v)
        
        parent = list(range(maxRow+maxCol+2))
        rank = [0]*(maxRow+maxCol+2)
        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]
        def union(u, v):
            ulp_u = find(u)
            ulp_v = find(v)
            if ulp_u == ulp_v: return
            if rank[ulp_u] > rank[ulp_v]:
                parent[ulp_v] = ulp_u
            elif rank[ulp_u] < rank[ulp_v]:
                parent[ulp_u] = ulp_v
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1
        
        hm = set()
        for row,col in stones:
            union(row, maxRow + col + 1)
            hm.add(row)
            hm.add(maxRow + col + 1)
        cnt = 0
        for i in hm:
            if find(i) == i:
                cnt+= 1
        return n-cnt

            
