class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        dist=[[float("inf")]*m for i in range(n)]
        dist[0][0]=0
        pq=[(0,0,0)] #effort, r,c
        while pq:
            effort,r,c=heapq.heappop(pq)
            if effort>dist[r][c]:
                continue
            if r==n-1 and c==m-1:
                return effort
            for dx,dy in directions:
                nx=r+dx
                ny=c+dy
                if 0<=nx<n and 0<=ny<m:
                    diff=abs(heights[nx][ny]-heights[r][c])
                    neweffort=max(effort,diff)
                    if neweffort<dist[nx][ny]:
                        dist[nx][ny]=neweffort
                        heapq.heappush(pq,(neweffort,nx,ny))
        return 0


        

        