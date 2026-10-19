class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist=[float("inf")]*(n+1)
        adj=defaultdict(list)
        for (u,v,w) in times:
            adj[u].append((v,w))
            # adj[v].append((u,w))
        dist[k]=0
        pq=[(0,k)] # (time,node)
        while pq:
            time,node=heapq.heappop(pq)
            if time>dist[node]:
                continue
            for neigh,weight in adj[node]:
                if dist[neigh]>time+weight:
                    dist[neigh]=time+weight
                    heapq.heappush(pq,(time+weight,neigh))
        # print(dist)
        mintime=float("-inf")
        for i in range(1,n+1):
            mintime=max(dist[i],mintime)
            # print(mintime)
        if mintime==float("inf"):
            return -1
        else:
            return mintime
        
        
