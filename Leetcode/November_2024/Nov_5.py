class Solution:
    def minChanges(self, s: str) -> int:
        res=0
        n=len(s)
        for i in range(0,n,2):
            if(s[i]!=s[i+1]):
                res+=1
        return res