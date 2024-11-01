class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        temp=[]
        l,r=0,len(arr)-1
        while(l<=r):
            temp.append(arr[l])
            l+=1
            if(l<=r):
                temp.append(arr[r])
                r-=1
        res=abs(temp[0]-temp[-1])
        for i in range(len(temp)-1):
            res+=abs(temp[i]-temp[i+1])
        return res