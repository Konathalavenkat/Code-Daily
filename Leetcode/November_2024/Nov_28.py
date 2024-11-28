import heapq
from typing import List
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dist=[[1e9]*n for _ in range(m)]
        heap=[]
        dist[0][0] = 0 if grid[0][0] == 0 else 1
        heap.append((dist[0][0],0,0))
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]
        while(heap):
            cost,x,y = heapq.heappop(heap)
            if(x==m-1 and y==n-1):
                return cost
            for i in range(4):
                row = x + dr[i]
                col = y + dc[i]
                if(0<=row<m and 0<=col<n and dist[row][col]> cost + grid[row][col]):
                    dist[row][col]=cost + grid[row][col]
                    heapq.heappush(heap,(dist[row][col],row,col))
        return -1

