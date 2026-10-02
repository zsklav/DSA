class Solution:
    def criticalConnections(self, n: int, graph: list[list[int]]) -> list[list[int]]:
        adjList=defaultdict(list)
        for u,v in graph:
            adjList[u].append(v)
            adjList[v].append(u)
        # ab 3 arrays chaiye
        low=[-1]*n
        # parent=[-1]*n
        firstEnc=[-1]*n
        time=0
        res=[]
        def dfs(u,parent):
            nonlocal time
            firstEnc[u]=time
            low[u]=time
            time+=1
            # u ke saare nodes traverse karne hai
            # two cases: visited or not visited
            for v in adjList[u]:
                if firstEnc[v]==-1:
                    dfs(v,u)
                    low[u]=min(low[v],low[u])
                    if low[v]>firstEnc[u]:
                        res.append([u,v])
            # case two: visited
                else:
                    if v!=parent:
                        low[u]=min(low[u],firstEnc[v])
        for u in range(n):
            if firstEnc[u]==-1:
                dfs(u,-1)
        return res


