class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr = set(arr)
        res = 0
        for i in arr:
            if(i-1 not in arr):
                cnt = 0
                while(i in arr):
                    cnt+=1
                    i+=1
                res = max(res,cnt)
        return res
