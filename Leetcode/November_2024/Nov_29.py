from typing import List
import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        def getmin(val,time):
            return val + (1 if val%2==time%2 else 0)
        if(grid[0][1]>1 and grid[1][0]>1):
            return -1
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        heap = []
        m,n = len(grid),len(grid[0])
        dist = [[1e9]*n for _ in range(m)]
        dist[0][0]=0
        heapq.heappush(heap,(0,0,0))
        while(heap):
            time,x,y = heapq.heappop(heap)
            if(x==m-1 and y==n-1):
                return time
            for i in range(4):
                row = x+dr[i]
                col = y+dc[i]
                if(0<=row<m and 0<=col<n and dist[row][col]>max(getmin(grid[row][col],time),time+1)):
                    dist[row][col] = max(getmin(grid[row][col],time),time+1)
                    heapq.heappush(heap,(dist[row][col],row,col))
        return dist[m-1][n-1] if dist[m-1][n-1]!=1e9 else -1