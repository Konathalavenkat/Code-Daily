class Solution:
    def pushZerosToEnd(self,arr):
     ind,n=0,len(arr)
     for i in range(n):
    	    if(arr[i]!=0):
             arr[ind]=arr[i]
             ind+=1
     for i in range(ind,n):
            arr[i]=0