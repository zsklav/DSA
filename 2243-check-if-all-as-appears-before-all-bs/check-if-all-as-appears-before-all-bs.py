class Solution:
    def checkString(self, s: str) -> bool:
        # last index of a
        # first index of b
        # if first<last: false
        # else true
        last=0
        first=float("inf")
        for i in range(len(s)):
            if s[i]=="a":
                last=i
            elif s[i]=="b":
                if i<first:
                    first=i
        print(last,first)
        if last<first:
            return True
        elif last>first:
            return False
        elif last==0 and first==0:
            return True
        