class Solution:

    def aggressiveCows(self, stalls, k):
        
        stalls.sort()
        l,r = 1,stalls[-1]-stalls[0]
        
        def ispossible(mid):
            cnt = 1
            prev = stalls[0]
            for i in range(1,len(stalls)):
                if(stalls[i]-prev>=mid):
                    prev = stalls[i]
                    cnt+=1
            return cnt>=k
        
        while(l<=r):
            mid = (l+r)//2
            if(ispossible(mid)):
                l = mid+1
            else:
                r = mid-1
        return r