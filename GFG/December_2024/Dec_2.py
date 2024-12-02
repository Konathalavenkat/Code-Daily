class Solution:
    def search(self, pat, txt):
        # code here
        lps=[0]
        length = 0
        n = len(pat)
        for i in range(1,n):
            while(length>=1 and pat[i]!=pat[length]):
                length= lps[length-1]
            length += 1 if pat[i]==pat[length] else 0
            lps.append(length)
        res=[]
        m = len(txt)
        length = 0
        for i in range(m):
            while(length>0 and pat[length]!=txt[i]):
                length = lps[length-1]
            length += 1 if pat[length]==txt[i] else 0
            if(length==n):
                res.append(i-n+1)
                length = lps[length-1]
        return res
        