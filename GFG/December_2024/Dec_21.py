class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, mat): 
        # code here
        n = len(mat)
        for i in range(n):
            mat[i].reverse()
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
        return mat