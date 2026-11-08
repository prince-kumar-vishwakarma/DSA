# 201. Topological sort or Kahn's algorithm


class Solution:
    def topoSort(self, V, adj):
        visited = [False]*V
        stack = []
        def dfs(node):
            visited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            stack.append(node)


        for i in range(V):
            if not visited[i]:
                dfs(i)
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans


