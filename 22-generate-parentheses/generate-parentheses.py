class Solution:
    def helper(self,curr,open,close,n,res):
        if len(curr)==2*n:
            res.append(curr)
            return
        if open<n:
            self.helper(curr+"(",open+1,close,n,res)
        if close<open:
            self.helper(curr+")",open,close+1,n,res)

    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.helper("",0,0,n,res)
        return res

        
        
        