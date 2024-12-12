from typing import List
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[-i for i in gifts]
        heapq.heapify(heap)
        res = 0
        for i in range(k):
            if(not heap):
                return 0
            heapq.heappush(heap,-1*math.floor(math.sqrt(-heapq.heappop(heap))))
        return -sum(heap)