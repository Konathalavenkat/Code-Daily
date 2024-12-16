from typing import List 
import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[val,i] for i,val in enumerate(nums)]
        heapq.heapify(heap)
        for _ in range(k):
            minvalue,ind = heapq.heappop(heap)
            minvalue*=multiplier
            nums[ind]=minvalue
            heapq.heappush(heap,[minvalue,ind])
        return nums