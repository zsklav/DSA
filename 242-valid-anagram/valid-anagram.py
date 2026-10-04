class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap1={}
        for i in s:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for j in t:
            if j in hashmap1:
                hashmap1[j]-=1
                if hashmap1[j]==0:
                    del hashmap1[j]
        # print(hashmap1)
        return len(hashmap1)==0
        