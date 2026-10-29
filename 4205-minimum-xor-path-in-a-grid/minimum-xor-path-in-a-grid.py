class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        # memo={}
        # def recursion(i,j,xor):
        #     if i>=n or j>=m:
        #         return float("inf")
        #     xor^=grid[i][j]
        #     if i==n-1 and j==m-1:
        #         return xor
        #     if (i,j,xor) in memo:
        #         return memo[(i,j,xor)]
        #     right=recursion(i,j+1,xor)
        #     down=recursion(i+1,j,xor)
        #     memo[(i,j,xor)]=min(right,down)
        #     return memo[(i,j,xor)]
        # return recursion(0,0,0)
        dp=[[set() for i in range(m)] for j in range(n)]
        # filing the inital row 0
        dp[0][0].add(grid[0][0])
        for j in range(1,m):
            for x in dp[0][j-1]:
                dp[0][j].add(x^grid[0][j])
        for i in range(1,n):
            for x in dp[i-1][0]:
                dp[i][0].add(x^grid[i][0])
        # print(dp)
        for i in range(1,n):
            for j in range(1,m):
                for x in dp[i-1][j]:
                    dp[i][j].add(x^grid[i][j])
                for x in dp[i][j-1]:
                    dp[i][j].add(x^grid[i][j])
        return min(dp[n-1][m-1])




