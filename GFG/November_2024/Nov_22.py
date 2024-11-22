class Solution:
    def maximumProfit(self, prices):
        # code here
        res=0
        m = prices[0]
        for i in prices:
            m = min(m,i)
            res = max(res, i - m)
        return res