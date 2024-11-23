class Solution:
    def getMinDiff(self,k, arr):
        # code here
        arr.sort()
        res=arr[-1]-arr[0]
        n=len(arr)
        for i in range(1,n):
            res=min(res,max(arr[i-1]+k,arr[n-1]-k)-min(arr[0]+k,arr[i]-k))
        return res