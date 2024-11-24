class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        res = -1e9
        prefix = 0
        for i in arr:
            prefix = max(prefix+i,i)
            res = max(prefix,res)
        return res