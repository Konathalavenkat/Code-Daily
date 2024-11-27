class Solution:
    def missingNumber(self,arr):
        n = len(arr)
        for i in range(n):
            while(0<arr[i]<=n and arr[arr[i]-1]!=arr[i]):
                temp = arr[i]
                arr[i]=arr[arr[i]-1]
                arr[temp-1]=temp
        for i in range(n):
            if(i!=arr[i]-1):
                return i+1
        return n+1