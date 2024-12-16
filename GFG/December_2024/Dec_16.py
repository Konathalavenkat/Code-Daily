class Solution:

    def kthElement(self, a, b, k):
        if(len(a)>len(b)):
            return self.kthElement(b,a,k)
        m,n = len(a),len(b)
        l,r = max(0,k-n),min(k,m)
        while(l<=r):
            mid1 = (l+r)//2
            mid2 = k-mid1
            l1=a[mid1-1] if mid1>0 else -1e9
            l2=b[mid2-1] if mid2>0 else -1e9
            r1 = a[mid1] if mid1<m else 1e9
            r2 = b[mid2] if mid2<n else 1e9
            
            if(l1>r2):
                r = mid1-1
            elif(l2>r1):
                l = mid1+1
            else:
                return max(l1,l2)
        return -1