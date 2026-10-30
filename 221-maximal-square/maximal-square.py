class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*m for i in range(n)]
        maxi=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    if i==0 or j==0:
                        dp[i][j]=1
                    else:
                        dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                    maxi=max(dp[i][j],maxi)
        return maxi*maxi
        