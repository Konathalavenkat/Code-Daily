class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        #Your code here
        d={}
        res = 0
        for i in arr:
            res+=d.get(target-i,0)
            d[i]=d.get(i,0)+1
        return res