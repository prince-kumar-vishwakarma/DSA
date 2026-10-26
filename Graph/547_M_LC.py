# 547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        ans = 0
        def dfs(curr):
            visited[curr] = True
            for i in range(n):
                if isConnected[curr][i] == 1 and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i)
        return ans
        

        