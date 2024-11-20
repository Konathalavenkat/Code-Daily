class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        d={'a':0,'b':0,'c':0}
        def check(d):
            for i in d:
                if(d[i]<k):
                    return False
            return True
        
        for i in s:
            d[i]+=1
        
        if(not check(d)):
            return -1
        
        left = 0
        res=len(s)
        n=len(s)
        for i,val in enumerate(s):
            d[val]-=1
            while(d[val]<k):
                d[s[left]]+=1
                left+=1
            res = min(res, n-(i-left+1))
        return res