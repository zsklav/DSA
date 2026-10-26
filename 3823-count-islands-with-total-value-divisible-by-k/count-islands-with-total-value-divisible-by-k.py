class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(-1,0),(1,0),(0,-1)]
        def dfs(i,j,count):
            visited[i][j]=True
            count+=grid[i][j]
            for dx,dy in directions:
                nx=i+dx
                ny=j+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]!=0 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    count=dfs(nx,ny,count)
            return count
        visited=[[False]*m for i in range(n)]
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and not visited[i][j]:
                    if dfs(i,j,0)%k==0:
                        count+=1
        return count
                    
                    