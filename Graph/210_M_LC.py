# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        visited = [0]*numCourses
        stack = []
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
            stack.append(u)
            return True
        for u in range(numCourses):
            if visited[u] == 0:
                if not topo(u):
                    return []
        
        return stack[::-1]

