class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float("inf")]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][j]=0
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
            dist[u][v]=w
            dist[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        counts=[]
        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1
            counts.append(count)
        mincount=min(counts)
        for i in range(n-1,-1,-1):
            if counts[i]==mincount:
                return i

