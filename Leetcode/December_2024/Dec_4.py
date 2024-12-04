class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m,n = len(str1),len(str2)
        ind1,ind2=0,0
        for ind1 in range(m):
            if(str1[ind1]==str2[ind2] or (str1[ind1]=='z' and str2[ind2]=='a') or (ord(str2[ind2])-ord(str1[ind1])==1)):
                ind2+=1
                if(ind2==n):
                    return True
        return False