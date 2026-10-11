class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n=len(s)
        ans=[float("inf")]*n
        for i in range(n):
            if s[i]==c:
                ans[i]=0
        print(ans)
        # nearest c to the right
        for i in range(n):
            for j in range(i+1,n):
                if ans[i]!=0 and ans[j]==0:
                    ans[i]=abs(i-j)
                    break
        for i in range(n):
            for j in range(i-1,-1,-1):
                if ans[i]!=0:
                    if ans[j]==0:
                        ans[i]=min(ans[i],abs(i-j))
                        break
        return ans


        