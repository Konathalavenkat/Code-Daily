class Solution:
    def subarrayXor(self, arr, k):
        # code here
        d= {}
        d[0]=1
        res = 0
        curr_xor = 0
        for i in arr:
            curr_xor ^= i
            res+=d.get(curr_xor^k,0)
            d[curr_xor]=d.get(curr_xor,0)+1
        return res