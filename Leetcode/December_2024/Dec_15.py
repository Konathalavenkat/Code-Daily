from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [[-(((i+1)/(j+1))-i/j),i,j] for i,j in classes]
        heapq.heapify(heap)
        for i in range(extraStudents):
            ratio,pa,total=heapq.heappop(heap)
            heapq.heappush(heap,[-((pa+2)/(total+2)-(pa+1)/(total+1)),pa+1,total+1])
        res = 0
        for i in heap:
            res+=i[1]/i[2]
        return res/len(heap)