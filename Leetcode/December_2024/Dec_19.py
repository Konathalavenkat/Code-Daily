from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxind=0
        res=0
        n=len(arr)
        for i in range(n):
            maxind=max(maxind,arr[i])
            if(i>=maxind):
                res+=1
                maxind=i
        return res
