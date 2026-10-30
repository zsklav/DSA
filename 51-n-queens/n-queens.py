class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # normal backtrack and checking ka question h
        board=[["."]*n for i in range(n)]
        res=[]
        def issafe(i,j):
            for r in range(i):
                if board[r][j]=="Q":
                    return False
                distance=i-r
                # upperleft diagonal
                if j-distance>=0:
                    if board[r][j-distance]=="Q":
                        return False
                # upperright diagonal
                if j+distance<n:
                    if board[r][j+distance]=="Q":
                        return False
            return True
        def backtrack(i):
            if i==n:
                res.append(["".join(row) for row in board])
                return
            for j in range(n):
                if issafe(i,j):
                    board[i][j]="Q"  
                    backtrack(i+1)   # Next row
                    board[i][j]="."
        backtrack(0)
        return res


