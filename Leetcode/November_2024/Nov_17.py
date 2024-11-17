from typing import List
from heapq import heappush as push
from heapq import heappop as pop
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=1e9
        sum = 0
        heap = [(0,-1)]
        for i,val in enumerate(nums):
            sum+=val
            push(heap,(sum,i))
            while(heap and (sum - heap[0][0]>=k)):
                res = min(res, i-pop(heap)[1])
        return res if res!= 1e9 else -1