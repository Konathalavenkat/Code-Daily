class Solution:
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
        # code here 
        def bin(arr,target):
            l,r = 0,len(arr)-1
            while(l<=r):
                mid = (l+r)//2
            if(arr[mid]==target):
                return True
            elif(arr[mid]<target):
                l=mid+1
            else:
                r = mid-1
            return False
        for i in range(len(mat)):
            if(mat[i][0]<=x<=mat[i][-1] and bin(mat[i],x)):
                return True
            return False