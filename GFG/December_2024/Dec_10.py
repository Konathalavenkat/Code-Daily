class Solution:
    def minRemoval(self, intervals):
        res=[]
        intervals.sort(key = lambda x:[x[1],x[0]])
        for l,r in intervals:
            if(not res or res[-1][1]<=l):
                res.append([l,r])
        return len(intervals)-len(res)