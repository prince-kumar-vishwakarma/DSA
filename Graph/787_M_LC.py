# 787. Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u,v,p in flights:
            adj[u].append((v, p))
        INF = 10**9
        dist = [INF]*n
        dist[src] = 0 
        queue = deque([(0, src, -1)])
        while queue:
            cost,city,stop = queue.popleft()
            for neighbour, price in adj[city]:
                if dist[neighbour] > cost + price and stop+1<=k:
                    dist[neighbour] = cost + price
                    queue.append((dist[neighbour], neighbour, stop+1))
        if dist[dst] == INF:
            return -1
        return dist[dst]


        