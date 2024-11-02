class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        d={}
        for i in range(k+1):
            if(d.get(arr[i],0)>0):
                return True
            d[arr[i]]=d.get(arr[i],0)+1
        for i in range(k+1,len(arr)):
            d[arr[i-k-1]]-=1
            if(d.get(arr[i],0)>0):
                return True
            d[arr[i]]=d.get(arr[i],0)+1
        return False