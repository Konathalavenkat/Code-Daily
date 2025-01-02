class Solution:
    def countSubarrays(self, arr, k):
        # code here
        d = {}
        prefix = 0
        d[0]=1
        res = 0
        for i in arr:
            prefix+=i
            res+=d.get(prefix-k,0)
            d[prefix]=d.get(prefix,0)+1
        return res
