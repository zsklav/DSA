class Solution:
    def minChanges(self, s: str) -> int:
        # making disjints sert of blocks two
        n=len(s)
        if n<=1:
            return 0
        count=0
        i=0
        j=1
        while j<n:
            sets=(s[i],s[j])
            print(sets)
            if s[i]!=s[j]:
                count+=1
            i=j+1
            j=i+1
        return count


