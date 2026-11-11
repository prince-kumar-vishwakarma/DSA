# 207. Course Schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
        visited = [0] * numCourses
        # 0 = Unvisited
        # 1 = Visiting
        # 2 = Visited
        def dfs(node):
            if visited[node] == 1:
                return False  # Cycle detected

            if visited[node] == 2:
                return True  # Already processed

            visited[node] = 1

            for neigh in adj[node]:
                if not dfs(neigh):
                    return False

            visited[node] = 2
            return True
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False

        return True


