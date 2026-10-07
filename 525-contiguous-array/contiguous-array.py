class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        balance=0
        balancedict={0:-1}
        maxi=0
        for i in range(n):
            if nums[i]==0:
                balance-=1
            else:
                balance+=1
            if balance in balancedict:
                maxi=max(maxi,i-balancedict[balance])
            else:
                balancedict[balance]=i
        return maxi
        
        
            