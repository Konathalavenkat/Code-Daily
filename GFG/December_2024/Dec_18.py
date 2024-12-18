class Solution:
    def findPages(self, arr, k):
        def possible(mid):
            cnt = 1
            curr = 0
            for i in arr:
                if(i+curr<=mid):
                    curr+=i
                else:
                    cnt+=1
                    curr=i
            return cnt<=k
        if(k>len(arr)):
            return -1
        l,r = max(arr),sum(arr)
        while(l<=r):
            mid = (l+r)//2
            if(possible(mid)):
                r = mid-1
            else:
                l = mid+1
        return l