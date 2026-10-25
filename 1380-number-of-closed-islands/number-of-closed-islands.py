class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    grid[i][j]="W"
                else:
                    grid[i][j]="L"
        # print(grid)
        def dfs(i,j):
            visited[i][j]=True
            isClosed=not(i==0 or j==0 or i==n-1 or j==m-1)
            for dx,dy in directions:
                nx=dx+i
                ny=dy+j
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]=="L" and not visited[nx][ny]:
                    isClosed=dfs(nx,ny) and isClosed
            return isClosed
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="L" and not visited[i][j]:
                    if dfs(i,j):
                        count+=1
        return count
