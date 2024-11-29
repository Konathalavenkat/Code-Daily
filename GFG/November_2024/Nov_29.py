
class Solution:
    def addBinary(self, s1, s2):
        m,n = len(s1),len(s2)
        res = ['0']*(max(m,n)+1)
        ind = max(m,n)
        p=0
        carry = 0
        while(p<m or p<n or carry):
            s = carry
            s += int(s1[m-p-1]) if p<m else 0
            s += int(s2[n-p-1]) if p<n else 0
            carry = s//2
            res[ind] = str(s%2)
            ind-=1
            p+=1
        ind = 0
        while(ind<max(m,n)+1 and res[ind]=='0'):
            ind+=1
        return ''.join(res[ind:])