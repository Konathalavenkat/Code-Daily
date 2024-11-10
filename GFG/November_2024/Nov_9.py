import heapq
class Solution:
    def getSum(self,s1,s2):
        res=[]
        m,n=len(s1),len(s2)
        carry=0
        ind1,ind2=m-1,n-1
        while(ind1>=0 or ind2>=0):
            s=carry
            s+=int(s1[ind1]) if ind1>=0 else 0
            s+=int(s2[ind2]) if ind2>=0 else 0
            ind1-=1
            ind2-=1
            res.append(str(s%10))
            carry=s//10
        while(carry):
            res.append(str(carry%10))
            carry//=10
        while(res and res[-1]=='0'):
            res.pop()
        if(not res):
            return "0"
        return ''.join(res[::-1])
    def minSum(self, arr):
        # code here
        heapq.heapify(arr)
        nums1=[]
        nums2=[]
        while(arr):
            nums1.append(heapq.heappop(arr))
            if(arr):
                nums2.append(heapq.heappop(arr))
        return self.getSum(nums1,nums2)