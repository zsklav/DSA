class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i>0 and j>0:
                    matrix[i][j]=matrix[i][j]+matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
                elif i>0 and j==0:
                    matrix[i][j]+=matrix[i-1][j]
                elif i==0 and j>0:
                    matrix[i][j]+=matrix[i][j-1]
        count=0
        for top in range(n):
            for bottom in range(top,n):
                hashmap={0:1}
                prefix=0
                arr=[]
                for j in range(m):
                    if top>0 and j>0:
                        value=matrix[bottom][j]-matrix[top-1][j]-matrix[bottom][j-1]+matrix[top-1][j-1]
                    elif top>0:
                        value=matrix[bottom][j]-matrix[top-1][j]
                    elif j>0:
                        value=matrix[bottom][j]-matrix[bottom][j-1]
                    else:
                        value=matrix[bottom][j]
                    arr.append(value)
                for val in arr:
                    prefix+=val
                    if prefix-target in hashmap:
                        count+=hashmap[prefix-target]
                    if prefix in hashmap:
                        hashmap[prefix]+=1
                    else:
                        hashmap[prefix]=1
        return count
                

                



