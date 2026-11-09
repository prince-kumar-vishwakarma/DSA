# 721. Accounts Merge


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [0]*n
        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            ulp_u = find(u)
            ulp_v = find(v)
            if ulp_u == ulp_v: return False
            if rank[ulp_u]>rank[ulp_v]:
                parent[ulp_v] = ulp_u
            elif rank[ulp_u]<rank[ulp_v]:
                parent[ulp_u] = ulp_v
            else:
                parent[ulp_v] = ulp_u
                rank[ulp_u] += 1
            return True
        
        hm = {}
        for an, account in enumerate(accounts):
            for i in range(1, len(account)):
                if account[i] in hm:
                    union(an, hm[account[i]])
                else:
                    hm[account[i]] = an
        
        merge = [[] for _ in range(n)]
        for key, val in hm.items():
            p = find(val)
            merge[p].append(key)
        ans = []
        for i,m in enumerate(merge):
            if m:
                ans.append([accounts[i][0]] + sorted(m))

        return ans



