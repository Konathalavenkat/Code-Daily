class Solution:
    def minIncrements(self, arr): 
        # Code here
        arr.sort()
        res=0
        prev=arr[0]
        for i in arr[1:]:
            if(prev>=i):
                res+=(prev+1-i)
                prev+=1
            else:
                prev=i
        return res