class Solution:
    def maxProduct(self,arr):
        prefix,suffix = 1,1
        res = -1e9
        n = len(arr)
        for i in range(n):
            prefix*=arr[i]
            suffix*=arr[n-1-i]
            res = max(res,max(prefix,suffix))
            if(prefix == 0):
                prefix = 1
            if(suffix == 0):
                suffix = 1
        return res