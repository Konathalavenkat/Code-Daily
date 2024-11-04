from collections import defaultdict
class Solution:
    def findTriplets(self, arr):
        # Your code here
        d=defaultdict(list)
        res=[]
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                if(0-arr[i]-arr[j] in d):
                    for k in d[0-arr[i]-arr[j]]:
                        res.append([k,i,j])
            d[arr[i]].append(i)
        return res