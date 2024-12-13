class Solution:
    def findMin(self, arr):
        #complete the function here
        n=len(arr)
        l,r=0,n-1
        while(l!=r and arr[l]==arr[r]):
            l+=1
        res = arr[l]
        while(l<=r):
            mid=(l+r)//2
            if(arr[mid]<=arr[r]):
                res=min(res,arr[mid])
                r=mid-1
            else:
                l=mid+1
        return res