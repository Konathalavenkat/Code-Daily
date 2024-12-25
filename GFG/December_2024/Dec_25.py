class Solution:
    def setMatrixZeroes(self, mat):
        zerorow = False
        zerocol = False
        m,n = len(mat),len(mat[0])
        for i in range(m):
            if(mat[i][0]==0):
                zerocol=True
                break
        for i in range(n):
            if(mat[0][i]==0):
                zerorow = True
                break
        for i in range(1,m):
            for j in range(1,n):
                if(mat[i][j]==0):
                    mat[i][0]=0
                    mat[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if(mat[i][0]==0 or mat[0][j]==0):
                    mat[i][j]=0
        if(zerorow):
            for i in range(n):
                mat[0][i]=0
        if(zerocol):
            for i in range(m):
                mat[i][0]=0
        return mat