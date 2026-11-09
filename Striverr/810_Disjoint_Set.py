# 810. Disjoint Set

class DisjointSet:
    def __init__(self, n: int):
        self.rank = [0]*(n)
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    def _find(self, u:int) -> int:
        if u == self.parent[u]:
            return u
        self.parent[u] = self._find(self.parent[u])
        return self.parent[u]

    def find(self, u: int, v: int) -> bool:
        return self._find(u) == self._find(v)


    def unionByRank(self, u: int, v: int) -> None:
        ulp_u = self._find(u)
        ulp_v = self._find(v)
        if ulp_u == ulp_v:
            return
        if self.rank[ulp_u] == self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        elif self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        else:
            self.parent[ulp_v] = ulp_u
     

    def unionBySize(self, u: int, v: int) -> None:
        ulp_u = self._find(u)
        ulp_v = self._find(v)
        if ulp_u == ulp_v:
            return
        if self.size[ulp_u] == self.size[ulp_v]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        elif self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
        else:
            self.parent[ulp_v] = ulp_u
