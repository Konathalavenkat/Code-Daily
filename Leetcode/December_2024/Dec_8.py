from typing import List
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        line = []
        for i,j,k in events:
            line.append([i,0,k])
            line.append([j,1,k])
        line.sort()
        res = 0
        maxleft = 0
        for i,j,k in line:
            if(j==0):
                res = max(res,k+maxleft)
            else:
                maxleft = max(maxleft,k)
        return res
