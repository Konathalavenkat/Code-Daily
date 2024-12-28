class Solution:
    def findTriplets(self, arr):
        # Your code here
        arr = sorted([(val,i) for i,val in enumerate(arr)])
        res = []
        n = len(arr)
        for i in range(n-2):
            l,r = i+1,n-1
            while(l<r):
                s = arr[l][0]+arr[r][0]+arr[i][0]
                if(s==0):
                    res.append(sorted([arr[l][1],arr[r][1],arr[i][1]]))
                    tempr = r-1
                    while(l<tempr and arr[r][0]==arr[tempr][0]):
                        res.append(sorted([arr[l][1],arr[tempr][1],arr[i][1]]))
                        tempr-=1
                    l+=1
                elif(s<0):
                    l+=1
                else:
                    r-=1
        return res