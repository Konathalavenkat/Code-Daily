class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        l,r = 0,n-1
        curr = k
        prev = 0
        for i in arr:
            if(i-prev>1):
                if(curr-(i-prev-1)>0):
                    curr-=(i-prev-1)
                else:
                    return prev+curr
            prev = i
        return prev+curr