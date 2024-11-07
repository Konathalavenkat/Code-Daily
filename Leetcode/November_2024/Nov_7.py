
from collections import defaultdict
from typing import List
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d=defaultdict(int)
        for i in candidates:
            mask=1
            while(mask<=i):
                if(i&mask>0):
                    d[mask]+=1
                mask<<=1
        return max(d.values())