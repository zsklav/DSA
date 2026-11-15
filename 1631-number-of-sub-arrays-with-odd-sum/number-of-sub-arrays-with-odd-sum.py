class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        evencount=1
        oddcount=0
        prefixsum=0
        count=0
        for i in range(len(arr)):
            prefixsum+=arr[i]
            if prefixsum%2==0:
                count=(count+oddcount)%mod
                evencount+=1
            else:
                count=(count+evencount)%mod
                oddcount+=1
        return count