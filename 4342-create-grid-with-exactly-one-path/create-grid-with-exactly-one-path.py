class Solution:
    def createGrid(self, n: int, m: int) -> list[str]:
        directions=[(0,1),(1,0)]
        grid=[["#"]*m for i in range(n)]
        queue=deque([(0, 0)])
        print(queue)
        while queue:
            i,j=queue.popleft()
            grid[i][j]="."
            if i==n-1 and j==m-1:
                 return ["".join(row) for row in grid]
            if j+1<m:
                queue.append((i,j+1))
            elif i+1<n:
                queue.append((i+1,j))
        return ["".join(row) for row in grid]


