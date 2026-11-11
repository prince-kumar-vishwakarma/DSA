# 
# 64. Alien Dictionary



class Solution:
    def findOrder(self, dict, N, K):
        adj = [[] for _ in range(K)]
        for i in range(N-1):
            s1, s2 = dict[i], dict[i+1]
            j = 0
            while j<len(s1) and j<len(s2):
                if s1[j] != s2[j]: break
                j += 1
            # Invalid prefix case
            if j == len(s2) and len(s1) > len(s2):
                return ""
            adj[ord(s1[j]) - ord("a")].append(
                ord(s2[j]) - ord("a")
            )

        visited = [0]*K
        ans = []
        def topo(u):
            if visited[u] == 1:
                return False
            if visited[u] == 2:
                return True
            visited[u] = 1
            for v in adj[u]:
                if not topo(v):
                    return False
            visited[u] = 2
            ans.append(u)
            return True
        for u in range(K):
            if visited[u] == 0:
                if not topo(u):
                    return ""
        ans.reverse()
        return "".join(chr(x + ord('a')) for x in ans)

            
       
