class Solution:
    def mySqrt(self, x: int) -> int:
        # mid se kam? toh search space l=1 r=4
        l=1
        r=x
        ans=x
        while l<=r:
            mid=(l+r)//2
            if mid*mid>x:
                r=mid-1
            else:
                ans=mid
                l=mid+1
        return ans
        

        