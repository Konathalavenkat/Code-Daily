from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        res=0
        mi,prev = prices[0],prices[0]
        for i in prices:
            if(i<prev):
                res+=prev - mi
                mi = i
            if(i<mi):
                mi = i
            prev = i
        return res + max(0,prev - mi)