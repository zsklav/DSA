class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions=[(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1)] # 8 directions
        if grid[n-1][n-1]==1 or grid[0][0]==1:
            return -1
        queue=deque([(0,0,1)]) #r,c,moves
        grid[0][0] = 1
        while queue:
            r,c,moves=queue.popleft()
            if r==n-1 and c==n-1:
                return moves
            for dx,dy in directions:
                nx=r+dx
                ny=c+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                    grid[nx][ny]=1
                    queue.append((nx,ny,moves+1))
        return -1
        

        