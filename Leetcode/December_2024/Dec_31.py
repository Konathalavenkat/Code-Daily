from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = {}
        def solve(i):
            if(i>=n):
                return 0
            if(i in memo):
                return memo[i]
            ans = 1e9
            for cost,cnt in zip(costs,[1,7,30]):
                ind = i+1
                while(ind<n and days[ind]-days[i]<cnt):
                    ind+=1
                ans = min(ans,cost+solve(ind))
            memo[i]=ans
            return ans
        return solve(0)