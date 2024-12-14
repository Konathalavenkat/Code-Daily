from typing import List 
import heapq
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        maxheap = []
        minheap = []
        res = 0
        for i in range(n):
            heapq.heappush(minheap,[nums[i],i])
            heapq.heappush(maxheap,[-nums[i],i])
            while(-maxheap[0][0]-minheap[0][0]>2):
                left+=1
                while(minheap and minheap[0][1]<left):
                    heapq.heappop(minheap)
                while(maxheap and maxheap[0][1]<left):
                    heapq.heappop(maxheap)
            res += i-left+1
        return res