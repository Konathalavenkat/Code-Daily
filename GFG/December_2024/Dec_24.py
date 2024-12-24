class Solution:

#Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
        # code here 
        m,n = len(mat),len(mat[0])
        l,r = 0,m*n-1
        while(l<=r):
            mid=(l+r)//2
            if(mat[mid//n][mid%n]<x):
                l = mid+1
            elif(mat[mid//n][mid%n]>x):
                r = mid-1
            else:
                return True
        return False