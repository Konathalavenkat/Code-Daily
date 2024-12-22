class Solution:
    def matSearch(self, mat, x):
        m,n = len(mat),len(mat[0])
        l,r = 0,n-1
        while(0<=l<m and 0<=r<n):
            if(mat[l][r]>x):
                r-=1
            elif(mat[l][r]<x):
                l+=1
            else:
                return True
        return False