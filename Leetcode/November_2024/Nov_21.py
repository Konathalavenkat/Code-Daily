from typing import List
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cells = [[0]*n for i in range(m)]
        for i,j in walls:
            cells[i][j]=2
        for i,j in guards:
            cells[i][j]=3
        for i in range(m):
            prevleft = False
            prevright = False
            for j in range(n):
                if(cells[i][j]==2):
                    prevleft=False
                elif(cells[i][j]==3):
                    prevleft = True
                elif(prevleft):
                    cells[i][j]=1
                
                if(cells[i][n-j-1]==2):
                    prevright = False
                elif(cells[i][n-j-1]==3):
                    prevright = True
                elif(prevright):
                    cells[i][n-j-1]=1
        
        for j in range(n):
            prevtop = False
            prevbottom = False
            for i in range(m):
                if(cells[i][j]==2):
                    prevtop=False
                elif(cells[i][j]==3):
                    prevtop = True
                elif(prevtop):
                    cells[i][j]=1
                
                if(cells[m-i-1][j]==2):
                    prevbottom = False
                elif(cells[m-i-1][j]==3):
                    prevbottom = True
                elif(prevbottom):
                    cells[m-i-1][j]=1
            
        res=0
        for i in range(m):
            for j in range(n):
                if(cells[i][j]==0):
                    res+=1
        
        return res
        


                    
        

        