class Solution:
    # Function to find hIndex
    def lowerbound(self,arr,target):
        l,r = 0,len(arr)
        while(l<=r):
            mid = (l+r)//2
            if(arr[mid]>=target):
                r=mid-1
            else:
                l=mid+1
        return l
    def hIndex(self, citations):
        #code here
        citations.sort()
        n=len(citations)
        l,r = 0,citations[-1]
        while(l<=r):
            mid = (l+r)//2
            if(n-self.lowerbound(citations,mid)>=mid):
                l = mid+1
            else:
                r = mid-1
        return r