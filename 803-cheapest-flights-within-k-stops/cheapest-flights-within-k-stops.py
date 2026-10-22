class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float("inf")]*n
        dist[src]=0
        adj=defaultdict(list)
        for u,v,w in flights:
            adj[u].append((v,w))
        for i in range(k+1):
            temp=dist.copy()
            for u in range(n):
                for v,w in adj[u]:
                    if dist[u] != float("inf"):
                        if temp[v]>dist[u]+w:
                            temp[v]=dist[u]+w
            dist=temp
        if dist[dst]==float("inf"):
            return -1
        return dist[dst]
        