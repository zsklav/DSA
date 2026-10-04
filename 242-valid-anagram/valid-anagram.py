class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashmap1={}
        hashmap2={}
        for i in s:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1
        for j in t:
            if j in hashmap2:
                hashmap2[j]+=1
            else:
                hashmap2[j]=1
        return hashmap1==hashmap2
        