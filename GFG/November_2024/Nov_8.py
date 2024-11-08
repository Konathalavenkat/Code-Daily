
class Solution:
    def minRepeats(self, s1, s2):
        lps=[0]
        length=0
        m,n=len(s1),len(s2)
        for i in range(1,n):
            while(length>0 and s2[i]!=s2[length]):
                length=lps[length-1]
            length+=1 if s2[i]==s2[length] else 0
            lps.append(length)
        ind=0
        res=1
        for i in range(m):
            if(ind==n):
                return 1
            while(ind!=0 and s1[i]!=s2[ind]):
                ind=lps[ind-1]
            ind+=1 if s1[i]==s2[ind] else 0
        def check(ind):
            res=0
            while(ind<n):
                if(ind+m<=n):
                    if(s1==s2[ind:ind+m]):
                        res+=1
                        ind+=m
                    else:
                        return -1
                else:
                    res+=1
                    for i in range(ind,n):
                        if(s2[i]!=s1[i-ind]):
                            return -1
                    break
            return res
        x=ind
        while(x!=-1):
            curr=check(x)
            if(curr==-1):
                if(x==0):
                    break
                else:
                    x=lps[x-1]
            else:
                return res+curr
        return -1
        
        
            
        
            
