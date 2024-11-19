class Solution:
    def nextPermutation(self, arr):
        # code here
        def reverse(arr,i,j):
            while(i<j):
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        
        n=len(arr)
        req = n-1
        flag=False
        while(req!=0):
            if(arr[req]>arr[req-1]):
                req-=1
                flag = True
                break
            req -= 1
        if(not flag):
            reverse(arr,0,n-1)
            return arr
        for i in range(n-1,req,-1):
            if(arr[i]>arr[req]):
                arr[i],arr[req]=arr[req],arr[i]
                reverse(arr,req+1,n-1)
                return arr
        
        reverse(arr,req+1,n-1)
        return arr