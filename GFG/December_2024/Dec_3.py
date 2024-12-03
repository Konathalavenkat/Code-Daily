class Solution:
    def minChar(self, s):
        rev = s[::-1]
        lps = [0]
        length = 0
        n = len(s)
        for i in range(1,n):
            while(length>0 and s[i]!=s[length]):
                length = lps[length-1]
            length+=1 if s[i]==s[length] else  0 
            lps.append(length)
        length = 0
        for i in range(n):
            while(length>0 and rev[i]!=s[length]):
                length = lps[length-1]
            length+=1 if rev[i]==s[length] else 0
            if(i!=n-1 and length==n):
                length= lps[length-1]
        return n - length