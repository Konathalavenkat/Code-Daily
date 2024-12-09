class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        res=[]
        l,r = newInterval
        intervals.sort()
        n = len(intervals)
        ind = 0
        while(ind<n and intervals[ind][1]<l):
            res.append(intervals[ind])
            ind+=1
        if(ind<n):
            if(intervals[ind][0]<=l<=intervals[ind][1]):
                intervals[ind][1]=max(intervals[ind][1],r)
            else:
                res.append([l,r])
            while(ind<n):
                if(not res or intervals[ind][0]>res[-1][1]):
                    res.append(intervals[ind])
                    ind+=1
                else:
                    res[-1][1]=max(res[-1][1],intervals[ind][1])
                    ind+=1
        else:
            res.append([l,r])
        return res