# 785. Is Graph Bipartite?

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        V = len(graph)
        color = [-1]*V
        
        
        for i in range(V):
            if color[i] != -1: continue

            queue = deque([i])
            color[i] = 0

            while queue:
                node = queue.popleft()
                for adj in graph[node]:
                    if color[adj] == -1:
                        color[adj] = 1 - color[node]
                        queue.append(adj)
                    elif color[adj] == color[node]:
                        return False
        return True

                





        